# mypy: disable-error-code=attr-defined
import os
import datetime as dt
from bot import Posts
from pathlib import Path
from enum import Enum
from typing import List
from logger import Logger
from sqlitewrapper import Row


__all__ = (
    'Flair',
    'get_flair',
    'modmail_removal_notification',
    'parse_cmd_line_args',
    'submission_is_older',
    'string_to_dt',
)


class Flair(Enum):
    SOLVED = 'Solved'
    ABANDONED = 'Abandoned'
    UKNOWN = 'Uknown'


def get_flair(flair: str) -> Flair:
    try:
        return Flair(flair)
    except ValueError:
        return Flair('Uknown')


def modmail_removal_notification(submission: Row, method: str) -> str:
    return f"""A post has been removed

OP: `{submission.username}`

Title: {submission.title}

Post ID: https://old.reddit.com/comments/{submission.post_id}

Date created: {submission.record_created}

Date found: {submission.record_edited}

Ban Template;    

    [Deleted post](https://reddit.com/comments/{submission.post_id}).    
        
    Deleting an answered post, without marking it solved, is against our rules.     

    You can read [our rules](https://reddit.com/r/MinecraftHelp/wiki/rules) to see if you're eligible to appeal this ban."""


# default template used when resetting the configuration.  this mirrors
# the template defined in ``config/config.py``; keeping a copy here avoids
# depending on the module itself being importable (which can fail if the
# directory is newly mounted or otherwise not part of sys.path).
DEFAULT_TEMPLATE = """# configuration for DeletedPosts bot
# edit the values of the dictionary below and restart the bot

config = {
    "client_id": "",
    "client_secret": "",
    "user_agent": "",
    "username": "",
    "password": "",
    "sub_name": "",
    # numeric settings are stored as integers here rather than strings
    "max_days": 180,
    "max_posts": 180,
    "sleep_minutes": 5,
}
"""

def parse_cmd_line_args(args: List[str], logger: Logger, config_file: Path, posts: Posts) -> bool:
    """Parse a very small set of operations from ``sys.argv``.

    ``config_file`` now refers to the Python configuration module path
    (typically ``.../config/config.py``).  ``reset_config`` will overwrite the
    file with a default template; the template is defined above to avoid
    importing the configuration module directly.
    """
    help_msg = """Command line help prompt
    Command: help
    Args: []
    Description: Prints the help prompt

    Command: reset_config
    Args: []
    Description: Overwrite the Python configuration file with default values

    Command: reset_db
    Args: []
    Description: Reset the database
"""
    if len(args) > 1:
        if args[1] == 'help':
            logger.info(help_msg)
        elif args[1] == 'reset_config':
            # write the default template text back to the configuration file.
            try:
                config_file.write_text(DEFAULT_TEMPLATE)
            except Exception:
                logger.error("Unable to reset configuration file")
        elif args[1] == 'reset_db':
            try:
                os.remove(posts.path)
            except FileNotFoundError:
                logger.error("No database found")
        else:
            logger.info(help_msg)
        return True
    return False


def submission_is_older(submission_date: dt.date, max_days: int) -> bool:
    current_date = dt.datetime.now().date()
    time_difference = current_date - submission_date
    if time_difference.days > max_days:
        return True
    return False


def string_to_dt(date_string: str) -> dt.datetime:
    return dt.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')

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


def parse_cmd_line_args(args: List[str], logger: Logger, config_file: Path, posts: Posts) -> bool:
    """Parse a very small set of operations from ``sys.argv``.

    ``config_file`` now refers to the Python configuration module path
    (typically ``.../config/config.py``).  ``reset_config`` will overwrite the
    file with the default template, which is imported from the configuration
    module itself so that it does not need to be duplicated here.
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
            # write the template text back to the configuration file.  import
            # TEMPLATE lazily in case the module has not yet been created.
            try:
                from config import TEMPLATE
                config_file.write_text(TEMPLATE)
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

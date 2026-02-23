"""
Configuration for the DeletedPosts bot.

This module exposes a single dictionary called ``config`` which holds all
of the parameters required to connect to Reddit and control the behaviour of
the bot.  When you first run the program the file will be created for you
with empty values; you should edit it before starting the bot.  You can also
reset the file to defaults by running the application with the
``reset_config`` command-line argument.

Example usage::

    from config import config
    print(config['client_id'])

"""

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

# same data as a text template.  both ``main.py`` and ``utils.actions`` import
# this so that the file can be created or reset without duplicating the
# literal configuration body.
TEMPLATE = f"""# configuration for DeletedPosts bot
# edit the values of the dictionary below and restart the bot

config = {config!r}
"""

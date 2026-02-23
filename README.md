# DeletedPosts Bot

Configuration used to live in a JSON file, but it has been migrated to a
Python module under ``config/config.py``.

When you first run the application a template file will be created for you in
the ``config`` directory.  Edit the values in the ``config`` dictionary and
restart the bot.

You can also reset the configuration back to the default template by invoking
``reset_config`` on the command line:

```
python -m Bot.main reset_config
```

Other command line actions (``help`` and ``reset_db``) remain unchanged.

# DeletedPosts Bot

## Description

DeletedPosts Bot monitors a specified subreddit for deleted posts and notifies moderators via modmail. It is designed to run continuously and can be easily deployed using Docker. Configuration is handled via environment variables or a Python config file.

## Quick Install (Docker)

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/DeletedPosts.git
   cd DeletedPosts
   ```

2. Copy `example.env` to `.env` and fill in your Reddit API credentials and bot settings:
   ```env
   CLIENT_ID=your_client_id_here
   CLIENT_SECRET=your_client_secret_here
   USER_AGENT="DeletedPostsBot/1.0 by YourUsername"
   USERNAME=bot_username
   PASSWORD=bot_password
   SUB_NAME=example_subreddit
   MAX_DAYS=180
   MAX_POSTS=180
   SLEEP_MINUTES=5
   ```

3. Use the provided `docker-compose.yml` file:
   ```sh
   docker-compose up -d
   ```

The bot will automatically generate its configuration from your environment variables each time the container starts.

---

## Advanced Install

If you want to customize the Docker setup or run the bot outside Docker:

1. Build your own Docker image:
   ```sh
   git clone https://github.com/yourusername/DeletedPosts.git
   cd DeletedPosts
   docker build -t deletedposts .
   ```

2. Create an `.env` file (or use `example.env`) with your Reddit API credentials and bot settings.

3. Run the container manually:
   ```sh
   docker run --env-file .env deletedposts
   ```

Or run the bot directly on your host:
   ```sh
   python Bot/main.py
   ```

---


You can  reset the configuration back to the default template by invoking
``reset_config`` on the command line:

```
python -m Bot.main reset_config
```

Other command line actions (``help`` and ``reset_db``) remain unchanged.

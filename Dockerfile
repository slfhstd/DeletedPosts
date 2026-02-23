FROM python:3.14-slim

WORKDIR /app

# Copy application files
COPY Bot ./Bot

RUN mkdir -p /app/config

# Install dependencies
RUN pip install --no-cache-dir praw 

ENV PYTHONUNBUFFERED=1

# Run the script
CMD ["python", "Bot/main.py"]

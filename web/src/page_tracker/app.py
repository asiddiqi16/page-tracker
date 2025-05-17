# src/page_tracker/app.py
"""This is a test app."""
import os
from functools import cache

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)


@app.get("/")
def index():
    """Root Index"""
    try:
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")
        return "Sorry, something went wrong \N{THINKING}", 500
    else:
        return f"This page has been seen {page_views} times."


@cache
def redis():
    """Return a redis client."""
    return Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

from math import log
from typer import Typer, Option
from dotenv import load_dotenv
from praw import Reddit
import logging
import time
import os

load_dotenv(".env")

app = Typer()

logger = logging.getLogger("reddit-multion")

reddit = Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)


@app.callback()
def setup_logging(
    log_level: str = Option(
        "INFO",
        "--log-level",
        "-l",
        help="Set the logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL",
    )
):
    """
    Set up logging configuration.
    """
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")

    # Create a formatter
    formatter = logging.Formatter("(%(asctime)s) [%(levelname)s]: %(message)s")

    # Create a handler
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    # Configure the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(numeric_level)
    root_logger.addHandler(handler)


@app.command()
def run(
    subreddit: str,
    n: int = Option(30, "--n", "-n", help="Number of posts to scan."),
):
    """
    This function determines where a promoting answer should be done,
    constructs a response based on MultiOn usecases and docs, and sends
    a response to a post.
    """

    subreddit_handle = reddit.subreddit(subreddit)

    for submission in subreddit_handle.new(limit=n):
        logging.info(
            f'Got a post to evaluate: "{submission.title}", URL: {submission.url}'
        )


@app.command()
def poll(
    subreddit: str,
    m: int = Option(30, "--m", "-m", help="Check for new posts each `m` minutes."),
    n: int = Option(30, "--n", "-n", help="Number of posts to scan."),
):
    """
    This function fetches new posts at the specified interval, determines
    if a promoting answer should be done, constructs a response based on
    MultiOn usecases and docs, and sends a response to the post if needed.
    """
    subreddit_handle = reddit.subreddit(subreddit)
    seen_posts = set()

    while True:
        logging.info("Fetching new posts...")
        for submission in subreddit_handle.new(limit=n):
            if submission.id not in seen_posts:
                seen_posts.add(submission.id)
                logging.info(
                    f'Got a post to evaluate: "{submission.title}", URL: {submission.url}'
                )
                # Add your logic to determine if a response should be made and send it

        time.sleep(m * 60)


def main():
    """
    Entry point for `poetry run app ...`
    """
    app()


if __name__ == "__main__":
    """
    Just in case the `app.py` is run through `python3 ...`
    """
    main()

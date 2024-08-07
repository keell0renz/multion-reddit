from typer import Typer, Option
from dotenv import load_dotenv

load_dotenv(".env")

app = Typer()


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
    print("Run with", n, subreddit)


@app.command()
def poll(
    subreddit: str,
    m: int = Option(30, "--m", "-m", help="Check for new posts each `m` minutes."),
):
    """
    This function fetches new posts at the specified interval, determines
    if a promoting answer should be done, constructs a response based on
    MultiOn usecases and docs, and sends a response to the post if needed.
    """
    print("Poll with", m, subreddit)


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

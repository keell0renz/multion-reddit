# Redditor MultiOn Bot

## Architecture

Has two modes, `run` and `poll`. When `run` is used, program scans first `N` specified posts in given subreddit, determines where a promoting answer should be done, constructs a response based on MultiOn usecases and docs, and sends a response to a post. When `poll` is used, the bot checks every `M` minutes specified for `N` new posts, and does same replying algorithm.

```bash
poetry run app run -n 20 webscraping
```

```bash
poetry run app poll -m 30 -n 30 webscraping
```

## Use

```bash
cd multion-reddit
```

```bash
poetry install
```

```bash
poetry run app ...
```

## Components

* Typer CLI framework + load of environment variables in `.env`
* MultiOn usecase description and docs in markdown format.
* Reddit API to fetch list of posts (either normally, or poll for new ones).
* MultiOn agent, goes to each post, detemines whether MultiOn usecase can be promoted, if yes -- constructs a natural-sounding response to the post with call to action.

## Algorithm

### `run`

1. Fetch first `N` post ids.
2. For each post id, create a url.
3. For each url, launch a MultiOn agent.
4. For each agent, pass the content of usecase description in markdown.
5. Task the agent to determine whether this post needs a response with MultiOn promotion.
6. If yes -- agent creates a reply to the post with the tailored explanation of how MultiOn can be used to solve user's problems.
7. If no -- exits the loop.

### `poll`

1. Each `M` minutes fetch new posts (compare to previous fetches and deterine new ones).
2. For each post id, create a url.
3. For each url, launch a MultiOn agent.
4. For each agent, pass the content of usecase description in markdown.
5. Task the agent to determine whether this post needs a response with MultiOn promotion.
6. If yes -- agent creates a reply to the post with the tailored explanation of how MultiOn can be used to solve user's problems.
7. If no -- exits the loop.

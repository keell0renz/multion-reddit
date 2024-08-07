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

## Warning

Due to the unreliable nature of MultiOn bot, which was intended to be a reasoning machine and API interacton engine, this script is a
mere prototype which just shows my intentions with using MultiOn, without actual MultiOn logic (because it's useless anyway).

If it was a real task, with no specific technology (MultiOn) to use, I would adjust the intended algorithm:

... Acquire all necessary posts to analyze from `run` or `poll`

1. Use LangChain + some LLM (GPT or Claude) to determine whether problem stated in the post can be solved using MultiOn (I would inject there adjusted prompt.py, but now only for True/False classification)
2. All posts who are classified as "True", I would again use LangChain + LLM to construct a tailored answer (Also inject adjusted prompt.py, but only for message generation.)
3. Post all constructed messages as a reply to the post using Reddit API.

Not to mention that this algorithm is done in parralel, like using `threading` because we have no need to do it for each post at a time.

This little project honestly does not need MultiOn bot, and even if we use it -- it does not work.

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

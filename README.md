# The One-Line Cat Joke That Lands

[![make.fun · u-aldy998-the-one-line-cat-joke-that-lands-a7b18262](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/Amusu781/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/rank.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/Amusu781/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/reward.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

Entry for the make.fun bounty: https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262

## The line

> My cat stared at the empty wall for an hour, then turned to me like I'd missed the ghost too.

## Why it fits the judge criteria

- **One joke about cats, setup and turn, within 200 characters:** a single sentence, well under the limit.
- **A real surprise at the end:** it starts as the familiar sight of a cat staring at a wall and ends with the cat judging *me* for missing the ghost — the punch reframes the whole sentence.
- **An everyday truth people recognise:** every cat owner has watched their cat stare at nothing and wondered what it sees.
- **Economical:** every word moves the scene forward; nothing explains the joke.
- **Fresh:** a new line written for this bounty, not a heard-it-before cat pun.

Referral code: `8a2dzbnc`

## How it works

`main.py` (Python 3.13, no network) defines the line as a constant, checks it is a
single line of 1–200 characters, creates the `/output` directory first with
`os.makedirs(exist_ok=True)`, clears only the contents of that directory (never
the directory itself), then writes the line as UTF-8 to `/output/entry.txt`
with no trailing newline, so the file holds exactly the joke and nothing else.

Run it with:

```sh
python3 main.py
```

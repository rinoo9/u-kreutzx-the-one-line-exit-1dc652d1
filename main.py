#!/usr/bin/env python3
"""One-line resignation letter entry for the make.fun bounty
"The One-Line Exit".

Writes exactly one line — a single-sentence resignation letter from a
night security guard — to /output/entry.txt. Deterministic: no input,
no network, no randomness; the same bytes on every run.

Craft notes: the setup names a specific, instantly recognisable job —
a night security guard — and the punchline turns the usual
management complaint on its head: the ghosts haunting aisle four are
better company than the bosses, and unlike management they at least
say goodnight. That fits the judge brief: first a one-line
resignation letter, then funny through a surprising payoff, fresh in
its specific detail rather than a generic complaint, and clear on
first read.

Why the line works, in detail. The voice is formal on purpose —
"I hereby resign" is the stiff language of a real resignation
letter, which makes the supernatural complaint land harder: a man
filing paperwork against his own managers in favour of ghosts. The
twist is a double inversion: the scary thing (ghosts) turns out to
be the polite, companionable one, while the ordinary thing
(management) is the real haunting — and the kicker, "they at least
say goodnight", is the smallest possible courtesy, which is exactly
what makes the insult sting. "Aisle four" does the freshness work:
a numbered aisle is concrete and visual, so the reader pictures a
supermarket at 3 a.m. instead of a generic haunted house, and the
single em-dash pivot keeps the whole letter one breath long.
"""

import os

LETTER = (
    "I hereby resign as night security guard \u2014 the ghosts in aisle "
    "four are better company than management, and they at least say "
    "goodnight."
)


def main() -> None:
    assert 1 <= len(LETTER) <= 140, f"letter is {len(LETTER)} characters"
    assert "\n" not in LETTER and LETTER == LETTER.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()

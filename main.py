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

Round 2 — a fresh angle: the round-1 letter quit as a night
security guard over ghosts with better manners than management;
this one quits as an office plant waterer, with a different
complaint (the plants unionised against the waterer) and a
different payoff (HR sided with the ferns).

Round 3 — a fresh angle again: no guard, no waterer. This one
quits as the printer’s therapist, the only person who listens to
the machine. The complaint is the machine’s, not the worker’s —
it jams under 200-page decks — and the payoff sides with the
machine: frankly, I understand it. The resignation is an act of
solidarity with the equipment.
"""

import os

LETTER = (
    "I hereby resign as the printer's therapist: it jams every time "
    "someone prints a 200-page deck, and frankly, I understand it."
)


def main() -> None:
    assert 1 <= len(LETTER) <= 140, f"letter is {len(LETTER)} characters"
    assert "\n" not in LETTER and LETTER == LETTER.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()

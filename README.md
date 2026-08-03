# Bowling kata in Python

[![CI](https://github.com/Coding-Cuddles/bowling-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/bowling-python-kata/actions/workflows/main.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

This kata complements [Clean Code: Fundamentals, Ep. 5 - Form](https://cleancoders.com/episode/clean-code-episode-5).

In bowling, a player rolls a ball down a lane and tries to knock down as many
pins as possible. The game consists of ten frames, and in each frame, the
player has two opportunities (called rolls) to knock down as many pins as
possible.

If, after two rolls, at least one pin is still standing, it’s called an **open
frame**. The score for the frame is the total number of pins knocked down,
plus bonus points awarded for strikes or spares.

A **spare** is when the player knocks down all the pins in two rolls. If the
player gets a spare, the score for the frame is ten, plus the number of pins
knocked down on their next roll. If a spare is thrown in the tenth frame, the
player is awarded one more roll.

A **strike** is when the player knocks down all the pins in one roll. If the
player gets a strike, their score for the frame is ten, plus the number of pins
knocked down on their next two rolls. If a strike is thrown in the tenth frame,
the player is awarded two more rolls.

The final score is the total of all frame scores.

## Instructions

In this kata, you will write a class `BowlingGame` that calculates the score of
a ten-pin bowling game with two methods:

1. `roll(pins)` is called each time the player rolls a ball, with
   `pins` representing the number of pins knocked down in the current roll;
2. `score()` returns the score calculated using the above rules.

## Examples

### Spare with a bonus

Here is an example of a game where the player gets a bonus after rolling a
spare:

```python
game.roll(7)
game.roll(3)  # Spare: 7 + 3 + 6 (bonus) = 16
game.roll(6)
game.roll(2)  # Open frame: 6 + 2 = 8

assert game.score() == 24
```

In this example, the player got a spare, which is ten plus the next roll. The
next roll (from the second frame) was a 6, so the value of the first frame is 16.
The second frame is worth exactly the number of pins the player knocked down.
Added to 16, it gives a total of 24.

### Perfect game

Here is an example of a game where the player gets the maximum score:

```python
for _ in range(12):
    game.roll(10)

assert game.score() == 300
```

In this example, the player gets 12 strikes in a row, the maximum number of
strikes possible in a game. Each strike is worth 10 points, plus the pins were
knocked down on the next two rolls, resulting in 300 points.

## Prerequisites

Required:

- [Git](https://git-scm.com/downloads)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Optional:

- [GNU Make](https://www.gnu.org/software/make/), for shorter commands. Every required task also
  has a direct `uv` command.

You do not need to install Python or pytest separately. `uv` installs a compatible Python version
and the locked project dependencies when needed.

## Set up the kata

1. Clone the repository:

   ```console
   git clone https://github.com/Coding-Cuddles/bowling-python-kata.git
   ```

2. Enter the repository directory:

   ```console
   cd bowling-python-kata
   ```

3. Run the starter test. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest test_*.py
   ```

   The first run may install Python and the project dependencies. Setup is complete when pytest
   reports `1 passed`.

   If the command fails with `uv: command not found`, install
   [uv](https://docs.astral.sh/uv/getting-started/installation/) and repeat this step.

## Work on the kata

1. Start with a bowling behavior in `test_bowling.py` and implement it in `bowling.py`.

2. Run the tests after each change. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest test_*.py
   ```

   Continue when the test run passes.

## Make command reference

Make is optional. Run `make` or `make help` to list these commands in the terminal.

| Command             | Result                                  |
| ------------------- | --------------------------------------- |
| `make all`          | Run the test suite                      |
| `make help`         | Show the command reference              |
| `make test`         | Run the test suite                      |
| `make format`       | Format tracked Python files             |
| `make format-check` | Check formatting without changing files |
| `make clean`        | Remove generated caches                 |

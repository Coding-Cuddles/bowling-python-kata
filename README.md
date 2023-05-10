# Bowling Python Kata

[![CI](https://github.com/Coding-Cuddles/bowling-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/bowling-python-kata/actions/workflows/main.yml)
[![Replit](https://replit.com/badge/github/Coding-Cuddles/bowling-python-kata)](https://replit.com/new/github/Coding-Cuddles/bowling-python-kata)

## Overview

This kata complements [Clean Code: Fundamentals, Ep. 5 - Form](https://cleancoders.com/episode/clean-code-episode-5).

In bowling, a player rolls a ball down a lane and tries to knock down as many
pins as possible. The game consists of ten frames, and in each frame, the
player has two opportunities (called rolls) to knock down as many pins as
possible.

If, after two rolls, at least one pin is still standing, it’s called an **open
frame**. The score for the frame is the total number of pins knocked down,
plus bonus points awarded for strikes or spares.

A **spare** is when the player knocks down all the pins in two rolls.  If the
player gets a spare, the score for the frame is ten, plus the number of pins
knocked down on their next roll. If a spare is thrown in the tenth frame, the
player is awarded one more roll.

A **strike** is when the player knocks down all the pins in one roll.  If the
player gets a strike, their score for the frame is ten, plus the number of pins
knocked down on their next two rolls. If a spare is thrown in the tenth frame,
the player is awarded two more rolls.

The final score is the total of all frame scores.

## Instructions

In this kata, you will write a class `BowlingGame` that calculates the score of
a game of ten-pin bowling with two methods:

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
next roll (from the second frame) was a 6, so the value of the first frame is
16. The second frame is worth exactly the number of pins the player knocked
down. Added to 16, it gives a total of 24.

### Perfect game

Here is an example of a game where the player gets the maximum score:

```python
for _ in range(12):
    game.roll(10)

assert game.score() == 300
```

In this example, the player gets 12 strikes in a row, the maximum number of
strikes possible in a game.  Each strike is worth 10 points, plus the pins were
knocked down on the next two rolls, resulting in 300 points.

## Usage

You can import this project into [Replit](https://replit.com), and it will
handle all dependencies automatically.

### Prerequisites

* [Python 3.8+](https://www.python.org/)
* [pytest](https://pytest.org)

### Run main

```console
make run
```

### Run tests

```console
make test
```

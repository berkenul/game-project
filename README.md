# Game Project — Group 11

A Python command-line arcade for Lab 1. Choose between a number guessing game and Rock-Paper-Scissors, play multiple rounds, switch games, or quit from the main menu.

## Team and contributions

| Team member | Contribution |
| --- | --- |
| Berk Enul | Guessing Game (`guessing.py`) and project integration |
| Han Bhone Hset | Rock-Paper-Scissors (`rps.py`) |
| Alex Sett | Main menu (`main.py`) |

## Run the project

Python 3 is required. No third-party packages are needed. From the project folder, run:

```bash
python3 main.py
```

Select `1` for the Guessing Game, `2` for Rock-Paper-Scissors, or `3` to quit. After a round, enter `Y` to return to the menu or `N` to exit. You can also test the games individually with `python3 guessing.py` and `python3 rps.py`.

## Games

- **Guessing Game:** Guess a random number from 1 to 100 within five valid attempts. The game gives higher/lower hints and reveals the answer after a loss. Invalid input does not use an attempt.
- **Rock-Paper-Scissors:** Choose `1` for paper, `2` for scissors, or `3` for rock. The computer chooses randomly, and the game reports the result and which move wins. Invalid choices are rejected.

## Project files

| Path | Purpose |
| --- | --- |
| `main.py` | Welcome message, game selection, and replay/exit menu |
| `guessing.py` | Number guessing game |
| `rps.py` | Rock-Paper-Scissors game |
| `test-cases/` | Terminal screenshots of wins, losses, ties, and invalid inputs |

The screenshots in `test-cases/` show the required win and loss outcomes for both games, plus additional input checks. The games were also tested through `main.py` to verify switching and replay.

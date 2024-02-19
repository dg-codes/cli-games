import random
from dataclasses import dataclass

from cli_games.utils.life_support import LifeSupport


@dataclass
class GameSettings:
    total_lives: int = 3
    range_start: int = 1
    range_end: int = 5


def run_game(settings: GameSettings):
    print(
        "I'm thinking of a number between",
        f"{settings.range_start} and {settings.range_end}.",
        f"Can you guess it? You have {settings.total_lives} tries.",
    )
    life_support = LifeSupport(settings.total_lives)

    number_to_guess = random.randint(settings.range_start, settings.range_end)

    player_guess = None

    while True:
        player_guess = int(input("Your guess is?\n"))

        if player_guess == number_to_guess:
            print(f"Correct! The number was {number_to_guess}.")
            break

        life_support.manage_hit()
        if life_support.is_dead:
            break

        print("Try again!")

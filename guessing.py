import random


def guessing_game(low=1, high=100, tries=5):
    """
    Andrew Hsia
    Play a guessing game using a randomly generated number.

    Give the player hints if their guess is too high or too low.
    End each round when they guess correctly or run out of tries,
    then ask whether they want to play again.

    Args:
        low (int): Smallest possible number. Defaults to 1.
        high (int): Largest possible number. Defaults to 100.
        tries (int): Number of guesses per round. Defaults to 5.

    Returns:
        None.
    """
    play_again = "Y"

    while play_again == "Y":
        number = random.randint(low, high)
        print(f"I'm thinking of a number between {low} and {high}.")
        prompt = f"Guess what it is. You have {tries} tries: "

        for tries_left in range(tries - 1, -1, -1):
            guess = int(input(prompt))

            if guess == number:
                print("You got it!")
                break

            if tries_left == 0:
                print(f"Nope! You lost. The number was {number}")
            else:
                if guess < number:
                    hint = "Too low."
                else:
                    hint = "Too high."

                word = "try" if tries_left == 1 else "tries"
                prompt = (
                    f"Nope! {hint} Try again "
                    f"({tries_left} {word} left): "
                )

        play_again = input(
            "Do you want to play again? (Y/N): "
        ).strip().upper()


if __name__ == "__main__":
    guessing_game()

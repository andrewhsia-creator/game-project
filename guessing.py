import random


def guessing_game(low=1, high=100, tries=5):
    """Play a number guessing game with limited tries and a replay option."""
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

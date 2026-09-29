import random


#Sean Coffin 

def rock_paper_scissors():
    #Rock Paper Scissors method
    play = input("Do you want to play? (yes/no): ")
    play = play.lower()

    if play != "yes":
        print("Okay, maybe next time!")
    while play == "yes":
        #Game keeps running as long as the player keeps saying "yes"
        
        #Takes user input and generates computer's choice
        guess = int(input("Enter your choice 1. paper, 2. scissors, or 3. rock): "))
        computer = random.randint(1, 3)

        #Checks for win conditions: 1 beats 3, 2 beats 1, 3 beats 2
        if guess == computer:
            print(f"Computer chose {computer}. It is a tie!")
        elif (guess == 1 and computer == 2) or (guess == 2 and computer == 3) or (guess == 3 and computer == 1):
            print(f"Computer chose {computer}. Computer wins!")
        else:
            print(f"Computer chose {computer}. You win!")
        play = input("Do you want to play again? (yes/no): ")
        play = play.lower()


    if __name__ == "__main__":
        rock_paper_scissors()


# (Rock paper scissors)
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock,paper,scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if (player >= 0 and player <= 2):
    print(game[player])

    print("Computer chose:")
    computer=random.randint(0,2)    #generates an integer between the range provided as argument to it

    print(game[computer])

    # conditional logic
    if (player == 0 and computer == 2):
        print("You win!")
    elif (player == 1 and computer == 0):
        print("You win!")
    elif (player == 2 and computer == 1):
        print("You win!")
    elif(player == 2 and computer == 0):
        print("You lose!")
    elif (computer > player):
        print("You lose!")
    elif (computer == player):
        print("Draw!")
else:
    print("You input an invalid number.. You lose!")
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

imagelist = [rock, paper, scissors]
gamelist = ["rock", "paper", "scissors"]

player_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")

if 0 <= int(player_input) <= 2:
  player_choice = gamelist[int(player_input)]
else:
  print("Oops! Something went wrong...")
print("You chose: \n"+imagelist[int(player_input)])

comp_input = random.randint(0,2)
comp_choice = gamelist[comp_input]
print("Computer chose: \n"+imagelist[int(comp_input)])

if player_choice == comp_choice:
  print("Draw.")
elif player_choice == "rock" and comp_choice == "scissors":
    print("You win!")
elif player_choice == "paper" and comp_choice == "rock":  
    print("You win!")
elif player_choice == "scissors" and comp_choice == "paper":  
    print("You win!")
else:
  print("You lose.")

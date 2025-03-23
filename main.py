import random
print("Welcome to the Rock, Paper, Scissors game:")
help = input("Press Enter to continue or type (Help) for the rules: ")
rock="""    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper=""" 
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
computer_choice=random.randint(0,2)
if help.lower() == "help":
  print("""********* RULES *********
 1)You choose and the computer chooses
 2)Rock smashes Scissors -> Rock wins
 3)Scissors cut Paper -> Scissors win
 4)Paper covers Rock -> Paper wins""")
  you_choose=input("Enter your choice (rock, paper, scissors): ").lower()
else:
  you_choose=input("enter your guess (rock, paper, scissors): ").lower()
if you_choose.lower() == "rock":
    print("you choose rock\n")
    print(rock)
elif you_choose.lower() == "paper":
    print("you choose paper\n")
    print(paper)
elif you_choose.lower() == "scissors":
    print("you choose scissors\n")
    print(scissors)
else:
  print("invalid choice")
if computer_choice == 0:
  computer_choice= rock
  print(f"computer choose rock\n \n{computer_choice}")
elif computer_choice == 1:
  computer_choice= paper
  print(f"computer choose paper\n \n{computer_choice}")
elif computer_choice == 2:
  computer_choice= scissors
  print(f"computer choose scissors\n \n{scissors}")

if you_choose == "rock" and computer_choice == rock:
  print("you are tied")
elif you_choose == "rock" and computer_choice == paper:
  print("you lost")
elif you_choose == "rock" and computer_choice == scissors:
  print("you win")
elif you_choose == "paper" and computer_choice == rock:
  print("you win")
elif you_choose == "paper" and computer_choice == paper:
  print("you are tied")
elif you_choose == "paper" and computer_choice == scissors:
  print("you lost")
elif you_choose == "scissors" and computer_choice == rock:
  print("you lost")
elif you_choose == "scissors" and computer_choice== paper:
  print("you win")
elif you_choose == "scissors" and computer_choice == scissors:
  print("you are tie")

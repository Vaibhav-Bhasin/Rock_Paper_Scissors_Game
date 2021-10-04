"""The computer will play the Rock, Paper, Scissors Game against you. This is purely the game of chance. Game rules are simple. Rock beats scissors, scissors beat paper, paper beats rock. Two of the same gives a draw. A. Implement a single round of the game. B. Ask the user how many rounds they want to play, between 3 and 6. C. Use random.choice(['rock','paper','scissors']) function to generate a random choices. D. Keep the score and show this at the end of the game. E. Check to make sure the user can only enter a number between 3 and 10. Otherwise, give them an error message. F. Personalise the experience with the player’s name."""
Rules for the Game

Rock beats Scissores
Scissores beats Paper
Paper beats Rock
........................................Purely a Game of Chance
Player=input("Please Enter Your Name :: \n")
rounds=int(input("Please Enter The Number Of Rounds You want To play \n" "Between 3 to 6:: \n"))
import random
if rounds in range(3,7):
  for i in range(rounds):
      Player=input("Please enter a Choice :: \n" "From Rock , Paper , Scissors \n")
      computer=random.choice(["Rock", "Paper" , "Scissors"])
      print("Computer choice:: \n",computer)
      if Player=="Rock" and computer=="Paper":
        print("Computer Won")
      elif Player=="Scissors" and computer=="Rock":
        print("Computer Won")
      elif Player=="Paper" and computer=="Scissors":
        print("Computer Won")
      elif Player=="Paper" and computer=="Paper":
        print("Tie")
      elif Player=="Rock" and computer=="Rock":
        print("Tie")
      elif Player=="Scissors" and computer=="Scissors":
        print("Tie")
      elif Player=="Rock" and computer=="Scissors":
        print("Player Won")
      elif Player=="Scissors" and computer=="Paper":
        print("Player Won")
      elif Player=="Paper" and computer=="Rock":
        print("Player Won")
      print()
else: 
  print("enter rounds between 3 and 6")

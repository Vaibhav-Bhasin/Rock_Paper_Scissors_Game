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

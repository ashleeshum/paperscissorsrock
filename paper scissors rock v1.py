#paper scissors rock
import random
# list of valid inputs that user can enter
valid_choices = ["p","s","r"]
# linking the p, s and r to the description
psr_map = {"p" : "paper", "s" : "scissors", "r" : "rock"}
# main while loop for whole game
while True:
  # asking user if they want to play the game
  user_answer = input("do you want to play a game of paper scissors rock? type y for yes and n for no: ")
  # if statement to run the game if user says yes
  if user_answer == "y":
    # while loop for users choice if they didn't enter valid input
    while True:
      # asking user to choose either p s or r
     user_choice = input("choose rock, paper or scissors. type r for rock, p for paper and s for scissors: ")
     # if statement to validate user input
     if user_choice in valid_choices:
       print("you have chosen", psr_map[user_choice], "!")
       # to do: put some random imported p s or r
    # if user didn't enter valid input then looped back to ask question again
     else:
       print("you haven't entered p s or r :/ try again: ")
  else:
    break 
print("alright, byebye")

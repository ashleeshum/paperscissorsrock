#paper scissors rock
import random
# list of valid inputs that user can enter
valid_answer = ["y","n"]
valid_choices = ["p","s","r"]
# linking the p, s and r to the description
psr_map = {"p" : "paper", "s" : "scissors", "r" : "rock"}
# made an undefined list in order to not use while true 
user_play = ""
# main while loop for whole game
while user_play == "":
  # asking user if they want to play the game
  user_answer = input("do you want to play a game of paper scissors rock? type y for yes and n for no: ")
  # if statement to run the game if user says yes
  if user_answer in valid_answer:
    # while loop for users choice if they didn't enter valid input
    while user_answer == "y":
      # asking user to choose either p s or r
     user_choice = input("choose rock, paper or scissors. type r for rock, p for paper and s for scissors: ")
     # if statement to validate user input
     if user_choice in valid_choices:
       print("you have chosen", psr_map[user_choice], "!")
       # to do: put some random imported p s or r
    # if user didn't enter valid input then looped back to ask question again
     else:
       print("you haven't entered p s or r :/ try again: ")
  if user_answer == "n":
    print("alright, byebye")
    break 
  else:
    print("you didn't enter y or n. try again: ")



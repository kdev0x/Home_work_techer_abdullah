import random
print("Rock Papper scissors Game")
class Computer:
 x = ""
 def __init__(self,amount_rounds):
   self.amount_rounds = amount_rounds

class User(Computer):
  def __init__(self , amount_rounds, user_choice = ""):
     super().__init__(amount_rounds)
     self.user_choice = user_choice

  def check_winner(self):
      user_score = 0
      computer_score = 0
      for round in range (0 , self.amount_rounds):
         game = ["rock","paper","scissors"]
         Computer.x = random.choice(game)

         user_choice = input("Rock Paper or Scissors")
         self.user_choice = user_choice
    
         if self.user_choice == Computer.x:
            print("You:", self.user_choice, "| Computer:", Computer.x)
            print("this round is a tie")

         elif self.user_choice == "rock" or self.user_choice == "Rock" and Computer.x == "scissors" or Computer.x =="scissors":
            print("You:", self.user_choice, "| Computer:", Computer.x)
            print("You won this round!")  
            user_score = user_score + 1

         elif self.user_choice == "rock" or self.user_choice == "Rock" and Computer.x == "paper" or Computer.x == "Paper":
            print("You:", self.user_choice, "| Computer:", Computer.x)
            print("You lost this round!")  
            computer_score = computer_score + 1

         elif self.user_choice == "paper" or self.user_choice == "Paper" and Computer.x == "rock" or Computer.x =="rock":
            print("You:", self.user_choice, "| Computer:", Computer.x)
            print("You won this round!")  
            user_score = user_score + 1

         elif self.user_choice == "paper" or self.user_choice == "Paper" and Computer.x == "scissors" or Computer.x == "Scissors":
            print("You:", self.user_choice, "| Computer:", Computer.x)
            print("You lost this round!")  
            computer_score = computer_score + 1

         elif self.user_choice == "paper" or self.user_choice == "Paper" and Computer.x == "rock" or Computer.x =="rock":
            print("You:", self.user_choice, "| Computer:", Computer.x)
            print("You won this round!")  
            user_score = user_score + 1

         elif self.user_choice == "scissors" or self.user_choice == "Scissors" and Computer.x == "paper" or Computer.x == "Paper":
            print("You:", self.user_choice, "| Computer:", Computer.x)
            print("You lost this round!")  
            computer_score = computer_score + 1

         elif self.user_choice == "scissors" or self.user_choice == "Scissors" and Computer.x == "rock" or Computer.x == "Rock":
            print("You:", self.user_choice, "| Computer:", Computer.x)
            print("You lost this round!")  
            computer_score = computer_score + 1
      if user_score > computer_score:
         print("[game summary] Your points:",user_score,"| computer points",computer_score,"\n You won")
      elif user_score < computer_score:
            print("[game summary] Your points:",user_score,"| computer points",computer_score,"\n You lost")
      else:
            print("[game summary] Your points:",user_score,"| computer points",computer_score,"\n It was a tie")




rounds = int(input("How many rounds would you like to play"))

computer_choise = User(rounds)
computer_choise.check_winner()




                  
         

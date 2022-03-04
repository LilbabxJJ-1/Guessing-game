import random
from termcolor import colored
import time
#variables

nums = []
number = random.randint(1,15)
nums.append(number)
turnsl = 6
turnst = 0


while True:
   try:
      rounds = int(input("How many rounds would you like to play? (Max is 10) "))
      if rounds > 10:
         print("That is too many rounds! Try again")
      elif rounds <= 0:
         print("You can't have less than 1 rounds! Try again")
      else:
         print(f"You have chosen {rounds} rounds\n")
         break
   except ValueError:
         print("That is not a number!")

print(colored("You have to guess a number between 1 and 15! Each turn, you'll get a hint to go higher or lower. You have 6 chances","cyan"))
      

#trials
a = 1
print(colored(f"\nRound {a}", "green"))
while a <= rounds:
   try:
      guess_number = int(input("\nWhat's your guess? "))
      if guess_number not in nums and turnsl != 1:
        turnsl -= 1
        turnst += 1
        print(colored(f"That is incorrect! {turnsl} more tries!","red"))
        with open("guesses.txt", "a") as guesses:
           guesses.write(f"Try {turnst}: {guess_number} \n")
        guesses.close
        if guess_number < number:
           print("Aim Higher!")
        else:
          print("Aim Lower!")  
  

      elif turnsl == 1 and number != guess_number:
          print(colored(f"\nYou failed!", "red"))
          print("Summary")
          with open("guesses.txt", "r") as guesses:
              print(guesses.read())
          guesses.close()
          print(f"Correct Number: {number}")

          with open("guesses.txt", "w") as guesses:
             guesses.write("")
          guesses.close()
          nums = []
          number = random.randint(1,15)
          nums.append(number)
          turnsl = 6
          turnst = 0
          if a == rounds:
            break
          else:
            a += 1
            print("Starting next round..")
            time.sleep(3)
            print(colored(f"\nRound {a}", "green"))
  
  #error and correct
      else:
         print(colored(f"You are correct! You guessed after {turnst} tries.", "green"))
         print("Summary")
         with open("guesses.txt", "r") as guesses:
            print(guesses.read())
         guesses.close()
         print(f"Correct Number: {number}")
        
         with open("guesses.txt", "w") as guesses:
             guesses.write("")
         guesses.close() 
         nums = []
         number = random.randint(1,15)
         nums.append(number)
         turnsl = 6
         turnst = 0
         if a == rounds: 
            break 
         else:
           a += 1
           print("Starting next round..")
           time.sleep(3)
           print(colored(f"\nRound {a}", "green"))
   except ValueError:
    print("That's not a number!")

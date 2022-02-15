import random

#variables
print("You have to guess a number between 1 and 15! Each turn, you'll get a hint to go higher or lower. You have 6 chances")
number = random.randint(1,15)
nums = []
nums.append(number)
turnsl = 6
turnst = 0


#trials
while True:
 try:
  guess_number = int(input("\nWhat's your guess? "))
  if guess_number not in nums and turnsl != 1:
   turnsl -= 1
   turnst += 1
   print(f"That is incorrect! {turnsl} more tries!")
   with open("guesses.txt", "a") as guesses:
     guesses.write(f"Try {turnst}: {guess_number} \n")
   guesses.close

   if guess_number < number:
     print("Aim Higher!")
   else:
     print("Aim Lower!")  
  

  elif turnsl == 1 and number != guess_number:
    
  
    print(f"\nYou failed!")
    print("Summary")

    with open("guesses.txt", "r") as guesses:
     print(guesses.read())
    guesses.close()
    print(f"Correct Number: {number}")

    with open("guesses.txt", "w") as guesses:
      guesses.write("")
    guesses.close()
    break
  
  #error and correct
  else:
   print(f"You are correct! You guessed after {turnst} tries.")
   print("Summary")

   with open("guesses.txt", "r") as guesses:
     print(guesses.read())
   guesses.close()
   print(f"Correct Number: {number}")

   with open("guesses.txt", "w") as guesses:
      guesses.write("")
   guesses.close()
   break
 except ValueError:
    print("That's not a number!")

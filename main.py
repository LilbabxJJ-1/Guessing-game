import random

#variables
print("You have to guess a number between 1 and 15! Each turn, you'll get a hint. You have 5 chances")
number = random.randint(1,15)
print(number)
nums = []
nums.append(number)
hint = 0
turnsl = 5
turnst = 0


#trials
while True:
 try:
  guess_number = int(input("\nWhat's your guess? "))
  if guess_number not in nums and turnsl != 1:
   hint += 1
   turnsl -= 1
   turnst += 1
   print(f"That is incorrect! {turnsl} more tries!")
   if guess_number < number:
     print("Aim Higher!")
   else:
     print("Aim Lower!")  

  elif turnsl == 1:
    print(f"You failed! The number was {number}!")
    break
  else:
   print(f"You are correct! You guessed after {turnst} tries")
   break
 except ValueError:
    print("That's not a number!")

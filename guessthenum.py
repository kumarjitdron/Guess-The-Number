from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
n=10
m=5
secret_num=random.randint(1,100)
def guess(chance):
	while chance>0:
		print(f"You have {chance} attemps remaining to guess the number.")
		guess=int(input("Make a guess: "))
		if guess>secret_num:
			print("Too high.")
			print("Guess again.")
		elif guess<secret_num:
			print("Too low.")
			print("Guess again.")
		elif guess==secret_num:
			print(f"You got it! The answer was {secret_num}")
			break
		chance=chance-1
	if chance==0 and guess!=secret_num:
		print("You've run out of guesses, You lose.")
if level=="easy":
	guess(n)
elif level=="hard":
	guess(m)
else:
	print("Enter correct difficulty")

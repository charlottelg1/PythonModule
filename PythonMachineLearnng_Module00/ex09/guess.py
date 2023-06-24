import random

if __name__ == "__main__":
	to_guess = random.randint(1, 99)
	# to_guess = 42
	trials = 0
	print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
		""")
	option = input("What's your guess beteween 1 and 99: \n")
	while (1):
		if option.isnumeric():
			if int(option) == to_guess:
				trials +=1
				if to_guess == 42:
					print("The answer to the ultimate question of life, the universe and everything is 42.")
				if trials == 1:
					print("Congratulations! You got it on your first try!")
				else:
					print("Congratulations, you've got it!")
					print (f'You won in : {trials} attempts !' )
				exit()
			if int(option) > to_guess:
				print("Too high!")
			elif int(option) < to_guess:
				print("Too low!")
		else:
			if option == "exit":
				print("Goodbye !")
				exit()
			elif not option.isnumeric():
				print("That's not a number.")
		trials += 1	
		option = input("What's your guess beteween 1 and 99: \n")	
		
		

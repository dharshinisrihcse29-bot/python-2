def number_guessing_game():
 print("Welcome to the Number Guessing Game!")
 lower = int(input("Enter the lower bound of the number: "))
 upper = int(input("Enter the upper bound of the number: ")) 
number_to_guess = lower + int(random.random() * (upper - lower + 1))
 attempts = 0
 guessed = False
 while not guessed:
 try:
 guess = int(input(f"Guess a number between {lower} and {upper}: "))
 attempts += 1
 if guess < number_to_guess:
 print("Too low! Try again.")
 elif guess > number_to_guess:
 print("Too high! Try again.")
 else:
 print(f" Congratulations! You guessed the number 
{number_to_guess} in {attempts} attempts.")
 guessed = True
 except ValueError:
 print("Please enter a valid integer.")
number_guessing_game()
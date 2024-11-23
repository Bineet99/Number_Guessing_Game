import random
number_to_guess = random.randint(1, 100)

print("Welcome to the Number Guessing Game")
print("I have selected a number between 1 and 100. Try to guess it!")

while True:
    user_guess=int(input("Enter the  number:"))
    if user_guess>100:
        print("You have entered the invalid number")
        break
    elif user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number")
        break

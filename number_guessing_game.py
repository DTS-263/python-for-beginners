import random
minRange = int(input("Enter your minimum range for picking a random number: "))
maxRange = int(input("Enter your maximum range for picking a random number: "))
number = random.randint(minRange, maxRange)
attempts = 0
maxAttempts = 10
while True:
    maxAttempts -= 1
    if (maxAttempts == 0):
        print(f"You exhausted all the available attempts, the correct number is {number}")
        break
    number_guessed = int(input(f"Guess the number between 1 and 100 in {maxAttempts} attempts: "))
    if number == number_guessed:
        print(f"You guessed the correct number in {attempts} attempts")
        break
    elif number > number_guessed:
        print("Guess a little higher")
    else:
        print("Guess a little lower")

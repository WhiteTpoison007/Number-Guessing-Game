import random

secret_number = random.randint(1, 10)

while True:
    print("what number am i thinking of ? between 1-10")
    guess = int(input("your guess?= "))
    
    # 1. Check for exit
    if guess == 11:
        print("Thanks for playing !")
        break
        
    # 2. Check for a correct guess
    elif guess == secret_number:
        print("Correct guess ! I'm picking a new number now...")
        secret_number = random.randint(1, 10) # Fresh number generated!
        
    # 3. Check if the guess is too high
    elif guess > secret_number:
        print("Too high! Try a smaller number.")
        
    # 4. Check if the guess is too low
    elif guess < secret_number:
        print("Too low! Try a bigger number.")
        
    print("-" * 40)
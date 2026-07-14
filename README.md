# Number-Guessing-Game
An endless, arcade-style Number Guessing Game built in Python. The computer selects a random number between 1 and 10, giving the player "too high" or "too low" hints until they guess correctly. Upon a correct guess, the game automatically generates a brand-new secret number so the fun never stops until the player chooses to exit

# Endless Number Guessing Game 🎮

A fun, interactive command-line game built in Python where you test your intuition against a random number generator. 

## 🚀 Features
* **Dynamic Hints:** The game guides you by telling you if your guess is too high or too low.
* **Endless Arcade Mode:** Guessing correctly doesn't kick you out! The computer instantly regenerates a new secret number so you can keep your winning streak alive.
* **Secret Exit:** Ready to stop? Type `11` at any time to gracefully close the game.

## 🛠️ Concepts Learned & Applied
Building this project helped me master several core Python fundamentals:
* **Loops:** Utilizing `while True` loops to create continuous game flow.
* **Conditional Logic:** Chaining `if` and `elif` structures to evaluate guess states dynamically.
* **Libraries:** Importing and utilizing the built-in `random` module to generate random integers.
* **Data Types:** Managing and casting user text inputs into integers using `int()`.

## 📦 How to Run
1. Make sure you have Python installed on your system.
2. Copy the code into a file named `main.py`.
3. Open your terminal or command prompt, navigate to the folder, and run:
   ```bash
   python main.py

## 🎮 How to Play
The game will prompt you to guess a number between 1 and 10.

Read the hints provided ("Too high" or "Too low") to adjust your next choice.

Keep guessing until you get it right!

To quit the game, type 11.

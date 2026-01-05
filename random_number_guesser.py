import random
import json
import os 
from datetime import datetime

def diff():
    while True:
        print("Welcome To Random Number Guesser")
        print("Choose Difficulty:")
        print("1. Baby (1-100)")
        print("2. Normal (1-1000)")
        print("3. Hard (1-10000)")
        print("4. View History")
        print("5. Exit")
        try:
            choice = int(input("Enter 1, 2, 3, 4 or 5: "))
            if choice in [1, 2, 3]:
                return choice
            elif choice == 4:
                display_his()
                continue
            elif choice == 5:
                print("Thanks for playing")
                return None
            else:
                print("Please enter 1, 2, 3, 4, or 5 only.")
        except ValueError:
            print("Invalid input! Number required.")

def range(difflvl):
    if difflvl == 1:
        return 100
    elif difflvl == 2:
        return 1000
    elif difflvl == 3:
        return 10000

def main():
    while True:
        lvl = diff()
        
        if lvl is None:
            break
            
        max_num = range(lvl)
        secret = random.randint(1, max_num)
        
        guessct = 0
        guess = 0

        while guess != secret:
            try:
                guess = int(input("Your guess: "))
                guessct += 1
                if guess > secret:
                    print("Too Big")
                elif guess < secret:
                    print("Too small")
                else:
                    print(f"You got it in {guessct} tries")
                    save(lvl, guessct, secret)
            except ValueError:
                print("Please enter a valid number")
        
        while True:
            again = input("Play again? (y/n) or History (h): ").lower()
            if again == 'y':
                break
            elif again == 'n':
                print("Thanks for playing")
                return
            elif again == 'h':
                display_his()
            else:
                print("Please enter y, n, or h")

def save(difficulty, tries, secret):
    record = {
        "difficulty": difficulty,
        "tries": tries,
        "secret": secret,
        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }
    if os.path.exists("game_history.json"):
        with open("game_history.json", "r") as f:
            history = json.load(f)
    else:
        history = []
    history.append(record)
    with open("game_history.json", "w") as f:
        json.dump(history, f, indent=2)

def load_his():
    if os.path.exists("game_history.json"):
        with open("game_history.json", "r") as f:
            return json.load(f)
    else:
        return []

def display_his():
    history = load_his()
    if not history:
        print("No games played yet")
        return
    print("\n--- Game History ---")
    for i, game in enumerate(history, 1):
        diff_name = {1: "Baby", 2: "Normal", 3: "Hard"}[game["difficulty"]]
        print(f"Game {i}: {diff_name} | Secret: {game['secret']} | Tries: {game['tries']} | {game['timestamp']}")
    print("--------------------\n")

if __name__ == "__main__":
    main()

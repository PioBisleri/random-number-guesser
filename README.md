# Random Number Guesser

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

A fun number guessing game with multiple difficulty levels and game history tracking. Test your luck and see how quickly you can guess the secret number!

## Features

- 🎮 Three difficulty levels:
  - **Baby** (1-100)
  - **Normal** (1-1000)
  - **Hard** (1-10000)
- 📜 Persistent game history tracking
- ⏱️ Timestamps for all game sessions
- 📊 Detailed statistics display
- 🔁 Option to replay or view history anytime

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/PioBisleri/random-number-guesser.git
   cd random-number-guesser
   ```

2. Run the game:
   ```bash
   python random_number_guesser.py
   ```

## Game Flow

1. Select difficulty level or view history
2. Guess the randomly generated number
3. Receive feedback ("Too Big" or "Too Small")
4. Win when you guess correctly!
5. Choose to play again, view history, or exit

## File Structure

```
random-number-guesser/
├── random_number_guesser.py  # Main game script
├── game_history.json         # Stores game history (auto-generated)
└── README.md                 # This documentation file
```

## Example Gameplay

```
Welcome To Random Number Guesser
Choose Difficulty:
1. Baby (1-100)
2. Normal (1-1000)
3. Hard (1-10000)
4. View History
5. Exit
Enter 1, 2, 3, 4 or 5: 1

Your guess: 50
Too Big
Your guess: 25
Too small
Your guess: 37
You got it in 3 tries!

Play again? (y/n) or History (h): h

--- Game History ---
Game 1: Baby | Secret: 37 | Tries: 3 | 05-01-2026 14:30:22
--------------------
```

## Requirements

- Python 3.7+
- Standard libraries only (`random`, `json`, `os`, `datetime`)

## License

MIT License - see [LICENSE](LICENSE) for details

---

*Created with ❤️ by [PioBisleri](https://github.com/PioBisleri)*  
*Happy guessing!* 🎲

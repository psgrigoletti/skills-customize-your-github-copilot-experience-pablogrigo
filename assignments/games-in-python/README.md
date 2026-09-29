# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic hangman game in Python using strings, loops, conditionals, and user input. This activity helps reinforce word manipulation, state tracking, and game flow control.

## 📝 Tasks

### 🛠️ Create the Word Selection and Game State

#### Descrição
Set up the initial game variables and choose a random secret word from a predefined list.

#### Requisitos
O programa concluído deve:

- Define a list of words and select one at random using `random.choice()`.
- Create variables to store the secret word, guessed letters, incorrect attempts, and maximum allowed mistakes.
- Display the current word state to the player using underscores for unrevealed letters.
- Keep the game state updated as the user makes guesses.

### 🛠️ Implement the Guessing Loop and End Conditions

#### Descrição
Build the main game loop so the player can guess letters until they either complete the word or run out of attempts.

#### Requisitos
O programa concluído deve:

- Ask the user for a letter input on each turn.
- Check whether the letter is in the secret word and update the visible progress.
- Count incorrect guesses and reduce the remaining attempts.
- Show feedback for correct and incorrect guesses.
- End the game when the player wins or loses, printing a final message with the result.

```python
# Example of expected game flow
# Word: _ _ _ _ _
# Guess a letter: p
# Correct! Word: p _ _ _ _
# Remaining attempts: 5
```
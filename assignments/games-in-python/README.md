# 📘 Assignment: Games in Python

## 🎯 Objective

Create a classic word-guessing game in Python using strings, loops, conditionals, and user input. This activity helps students practice state tracking, random selection, and game flow control.

## 📝 Tasks

### 🛠️ Create the Secret Word and Game State

#### Descrição
Set up the list of possible words and initialize the variables needed to track the player's progress during the game.

#### Requisitos
O programa concluído deve:

- Define a list of words and select one at random using `random.choice()`.
- Create variables to store the secret word, guessed letters, remaining attempts, and the current hidden word display.
- Show the initial board to the player using underscores to represent unrevealed letters.
- Keep the game state updated after every guess.

### 🛠️ Implement the Guessing Loop and Win/Lose Conditions

#### Descrição
Build the main game loop so the player can enter letters until the word is fully revealed or the number of mistakes reaches the limit.

#### Requisitos
O programa concluído deve:

- Ask the player to enter one letter at a time.
- Check whether the letter is in the secret word and update the visible word accordingly.
- Count incorrect guesses and reduce the remaining attempts.
- Print feedback for correct and incorrect guesses.
- End the game when the player wins or loses and display the final result.

```python
# Example of expected game flow
# Word: _ _ _ _ _
# Guess a letter: p
# Correct! Word: p _ _ _ _
# Remaining attempts: 5
```
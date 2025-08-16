# Key Clash

**Key Clash** is a simple text-based game built using Python where two players compete against each other by pressing specific keys to increase or decrease their scores. The game continues until the **"esc"** key is pressed, and the player with the highest score wins.

---

## Features:
- **Player 1** uses the `w` or `up` key to increase their score.
- **Player 2** uses the `s` or `down` key to increase their score.
- The game keeps track of the score for both players.
- Press **esc** to exit the game and see the winner.
- In case of a tie, the game announces it as a draw.

---

## How to Play:
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip` (described below).
3. Run the Python script.
4. Player 1 presses the **`w`** or **`up`** key to increase their score.
5. Player 2 presses the **`s`** or **`down`** key to increase their score.
6. Press the **`esc`** key to exit the game and see the winner's score.
7. The game announces the winner or if it’s a draw.

---

## Installation:

### Prerequisites:
- Python 3.x (Any version >= 3.6)
- `keyboard` module for detecting keypresses.

### Steps:
1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/KeyClash.git
    cd KeyClash
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

    If `requirements.txt` doesn't exist, simply install `keyboard` using:

    ```bash
    pip install keyboard
    ```

3. Run the game:

    ```bash
    python key_clash_game.py
    ```

---

## Usage:

Once the game starts:
- **Player 1** presses **`w`** or **`up`** to increase their score.
- **Player 2** presses **`s`** or **`down`** to increase their score.
- The current score is displayed on the screen after each key press.
- To exit the game and see the final result, press the **`esc`** key.

---

## Example of Gameplay:


---

## License:

This project is open-source and available under the [MIT License](LICENSE).

Feel free to contribute and make improvements!

---

## Contributing:

1. Fork this repository.
2. Create a branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new Pull Request.

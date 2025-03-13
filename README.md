# Planes Game

## Overview
Planes Game is a strategy-based guessing game, similar to Battleships, but with a unique twist: instead of ships of different sizes, players must locate and shoot down three planes hidden on a grid. A plane can only be eliminated by successfully identifying and hitting its **head/cockpit**.

This project was developed in **Python** as part of my final homework for the **Fundamentals of Programming** course in my first year of university.

## AI Algorithm
The AI opponent in this game is powered by a **custom function that I designed**, inspired by the **probability density function used in Battleship's smart AI**. This function has been adapted to fit the unique mechanics of the Planes Game, allowing the AI to make **strategic moves** based on probability rather than random guessing, improving its accuracy and efficiency over time.

## Installation Instructions
To play the game, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dosqas/Planes-Game.git
   cd Planes-Game
   ```

2. **Ensure you have Python installed** (version 3.x recommended). You can check your Python version with:
   ```bash
   python --version
   ```

3. **Install required dependencies**. Run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the game**:
   ```bash
   python main.py
   ```

## How to Play
- The game is played on a 10x10 grid where three planes are hidden.
- Your goal is to locate the **heads** of all three planes by making strategic guesses.
- The AI opponent will also try to find your planes using an advanced probability-based algorithm.
- The first player to shoot down all enemy planes wins!

## Repository
The full source code is available at: [Planes Game GitHub Repository](https://github.com/dosqas/Planes-Game)

## Contact
For any questions, suggestions, or issues, feel free to reach out to me:
- **Email**: [sebastian.soptelea@proton.me](mailto:sebastian.soptelea@proton.me)

Enjoy the game and have fun strategizing! 🚀


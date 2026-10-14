# Tic-Tac-Toe AI | Minimax & Alpha-Beta Pruning

A command-line Tic-Tac-Toe game where users play against an AI opponent using Minimax with alpha-beta pruning.

## Features
- Minimax algorithm for optimal move selection
- Alpha-beta pruning to eliminate unnecessary searches
- Win, loss and draw detection
- Displays the possible outcomes of available moves
- Human vs. AI gameplay

## How It Works
The AI recursively explores possible game states using Minimax. It assumes both players make optimal decisions and selects moves that maximize its outcome.

Alpha-beta pruning improves search efficiency by skipping branches that cannot affect the final decision.

## Running the Game
```bash
python TicTacToe_alphabeta.py
```

The game runs directly in the terminal.

# 🐭 Trap the Mouse
Trap the Mouse is a strategy-based game built in Python with a graphical interface using Tkinter. The game can be played in both Single-Player mode (against AI) and Two-Player mode, where one player controls the mouse, and the other places obstacles to trap it.

## 🎮 Game Modes
### 1. Single-Player Mode (vs AI) 🧠
In this mode, the player sets obstacles on the board while an AI-controlled mouse tries to escape. The AI has three difficulty levels:

🟢 Easy : The mouse moves randomly.

🟡 Medium : The mouse uses the BFS (Breadth-First Search) algorithm to find a path to the edge.

🔴 Hard : The mouse uses A* Search Algorithm with heuristics to navigate obstacles and find the best escape route.

### 2. Two-Player Mode 👥
Player 1 places obstacles to trap the mouse.

Player 2 controls the mouse and tries to escape to an edge.

## 🖥️ Tech Stack
### Language: Python 🐍
### GUI Framework: Tkinter 🎨
### Algorithms Used:
- Random movement (Easy AI)
- Breadth-First Search (BFS) (Medium AI)
- A* Search Algorithm with heuristics (Hard AI)

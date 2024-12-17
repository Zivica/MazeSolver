# Maze Generator and Solver with Real-Time Visualization

This project is a **Maze Generator and Solver** written in Python. It generates random mazes using the **recursive backtracking algorithm** and solves them using **Breadth-First Search (BFS)**. The program also includes a **real-time visualization** of the BFS solving process using `matplotlib`.

---

## Features

- **Maze Generation**:
  - Random maze creation using recursive backtracking.
- **Maze Solving**:
  - Solves the maze using BFS to find the shortest path.
- **Real-Time Visualization**:
  - Visualizes the BFS process step-by-step as it explores the maze.
  - Highlights:
    - **Visited cells** in blue.
    - **Solution path** in gold.
    - Start (green) and end (red) positions.

---

## Installation

1. Install Python (3.6 or later).
2. Install required libraries:

   ```bash
   pip install matplotlib
   ```

---

## How It Works

1. **Maze Generation**:
   - The maze is a grid of cells where each cell has 4 walls (top, right, bottom, left).
   - Recursive backtracking removes walls between cells to create a maze with connected paths.

2. **Maze Solving**:
   - Breadth-First Search (BFS) explores the maze step-by-step.
   - It finds the shortest path from the start to the end of the maze.

3. **Visualization**:
   - The maze is displayed in real time as the BFS algorithm runs.
   - Visited cells and the final path are highlighted.

---

## How to Run

1. Save the code as `maze_solver.py`.
2. Run the script:

   ```bash
   python maze_solver.py
   ```

3. The program will:
   - Generate a `20x20` maze.
   - Solve the maze using BFS.
   - Show the maze-solving process in real-time.

---

## Customize the Maze

You can customize the maze size and start/end positions by editing these lines:

```python
maze = Maze(width=30, height=30, start=(0,0), end=(29,29))
```

- `width` and `height`: Size of the maze grid.
- `start`: Starting coordinates (row, column).
- `end`: Ending coordinates (row, column).

---

## Example Output

### Visualization

- **Start position**: Green
- **End position**: Red
- **Visited cells**: Blue
- **Final Path**: Gold

Example Screenshot:
![Maze Visualization](example_maze.png)

---

## Code Overview

### Key Methods

- `generate_maze()`: Generates the maze using recursive backtracking.
- `solve_maze_bfs()`: Solves the maze using BFS.
- `bfs_stepwise()`: A generator to visualize BFS step-by-step.
- `visualize_maze(ax)`: Draws the maze grid.
- `visualize_realtime_bfs()`: Visualizes the maze-solving process in real-time.

---

## Dependencies

- **Python 3.6+**
- **matplotlib**

Install dependencies with:

```bash
pip install matplotlib
```

---

## License

This project is licensed under the **MIT License**. See the LICENSE file for details.

---

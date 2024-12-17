import random
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Maze:
    """
    Maze Generator and Solver with real-time visualization

    This class generates a maze using recursive backtracking and can solve the maze using BFS.
    It provides a method to visualize the maze-solving process step-by-step in real-time.
    """

    def __init__(self, width=20, height=20, start=(0,0), end=None):
        self.width = width
        self.height = height
        self.start = start
        self.end = end if end is not None else (height-1, width-1)

        # Each cell: walls as [top, right, bottom, left]
        # True = wall, False = no wall
        self.grid = [[[True, True, True, True] for _ in range(self.width)] for _ in range(self.height)]
        self.visited = [[False]*self.width for _ in range(self.height)]

    def generate_maze(self):
        """
        Generate the maze using the recursive backtracking algorithm.
        """
        stack = [self.start]
        self.visited[self.start[0]][self.start[1]] = True

        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        while stack:
            r, c = stack[-1]
            neighbors = []
            for i, (dr, dc) in enumerate(directions):
                nr, nc = r+dr, c+dc
                if 0 <= nr < self.height and 0 <= nc < self.width and not self.visited[nr][nc]:
                    neighbors.append((i, nr, nc))

            if neighbors:
                i, nr, nc = random.choice(neighbors)
                # Remove walls between current and chosen
                self.grid[r][c][i] = False
                opposite = (i+2)%4
                self.grid[nr][nc][opposite] = False
                self.visited[nr][nc] = True
                stack.append((nr, nc))
            else:
                stack.pop()

    def solve_maze_bfs(self):
        """
        Solve the maze using BFS and return the path.
        """
        start = self.start
        end = self.end
        queue = deque([start])
        visited = [[False]*self.width for _ in range(self.height)]
        visited[start[0]][start[1]] = True
        parent = {start: None}

        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        while queue:
            r, c = queue.popleft()
            if (r,c) == end:
                path = []
                curr = end
                while curr is not None:
                    path.append(curr)
                    curr = parent[curr]
                path.reverse()
                return path

            for i, (dr, dc) in enumerate(directions):
                nr, nc = r+dr, c+dc
                if 0 <= nr < self.height and 0 <= nc < self.width and not visited[nr][nc]:
                    if not self.grid[r][c][i]:
                        visited[nr][nc] = True
                        parent[(nr, nc)] = (r, c)
                        queue.append((nr, nc))

        return None

    def bfs_stepwise(self):
        """
        A generator function that yields the BFS frontier step-by-step.
        At each step, it yields (current_cell, visited_matrix, parent_dict).
        Used for real-time visualization.
        """
        start = self.start
        end = self.end
        queue = deque([start])
        visited = [[False]*self.width for _ in range(self.height)]
        visited[start[0]][start[1]] = True
        parent = {start: None}

        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        while queue:
            r, c = queue.popleft()

            # Yield current state
            yield (r, c, visited, parent)

            if (r,c) == end:
                return  # Reached the end

            for i, (dr, dc) in enumerate(directions):
                nr, nc = r+dr, c+dc
                if 0 <= nr < self.height and 0 <= nc < self.width and not visited[nr][nc]:
                    # Check for no wall
                    if not self.grid[r][c][i]:
                        visited[nr][nc] = True
                        parent[(nr, nc)] = (r, c)
                        queue.append((nr, nc))

    def reconstruct_path(self, parent):
        path = []
        curr = self.end
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        return path

    def visualize_maze(self, ax):
        """
        Draw the maze structure (walls) on the given axes.
        """
        # Draw the maze grid
        for r in range(self.height):
            for c in range(self.width):
                x = c
                y = self.height - r - 1
                if self.grid[r][c][0]:
                    ax.plot([x, x+1], [y+1, y+1], color='black')
                if self.grid[r][c][1]:
                    ax.plot([x+1, x+1], [y, y+1], color='black')
                if self.grid[r][c][2]:
                    ax.plot([x, x+1], [y, y], color='black')
                if self.grid[r][c][3]:
                    ax.plot([x, x], [y, y+1], color='black')

        # Highlight start and end
        sx, sy = self.start[1], self.height - self.start[0] - 1
        ex, ey = self.end[1], self.height - self.end[0] - 1
        ax.plot(sx+0.5, sy+0.5, marker='o', color='green', markersize=10, label='Start')
        ax.plot(ex+0.5, ey+0.5, marker='o', color='red', markersize=10, label='End')

    def visualize_realtime_bfs(self):
        """
        Visualize the BFS search in real-time as it explores the maze.
        Cells visited by BFS will be highlighted step-by-step.
        Once the end is found, the final path will be drawn.
        """
        plt.ion()
        fig, ax = plt.subplots(figsize=(self.width/2, self.height/2))
        ax.set_aspect('equal')
        ax.axis('off')
        self.visualize_maze(ax)

        # We'll use a scatter plot for visited cells
        visited_cells_x = []
        visited_cells_y = []
        visited_scatter = ax.scatter(visited_cells_x, visited_cells_y, s=100, c='blue', alpha=0.5, label='Visited')

        # Step through BFS
        gen = self.bfs_stepwise()
        parent = None
        end_found = False

        for (r, c, visited, p) in gen:
            parent = p
            if (r, c) == self.end:
                end_found = True
                break

            # Mark this cell as visited
            vx = c+0.5
            vy = self.height - r - 1 + 0.5
            visited_cells_x.append(vx)
            visited_cells_y.append(vy)
            visited_scatter.set_offsets(list(zip(visited_cells_x, visited_cells_y)))

            ax.legend()
            plt.draw()
            plt.pause(0.05)  # pause to update the figure

        # Once done, if we found the end, draw the path
        if end_found and parent is not None:
            path = self.reconstruct_path(parent)
            path_x = [c+0.5 for (r,c) in path]
            path_y = [self.height - r - 1 + 0.5 for (r,c) in path]
            ax.plot(path_x, path_y, color='gold', linewidth=2, label='Path')
            ax.legend()
            plt.draw()

        plt.ioff()
        plt.show()


if __name__ == "__main__":
    maze = Maze(width=20, height=20, start=(0,0), end=(19,19))
    maze.generate_maze()
    maze.visualize_realtime_bfs()

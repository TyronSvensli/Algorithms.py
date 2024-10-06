Matrix Generation:
The script generates a 2D matrix (grid) with a random number (0-10) at each cell.
The user has the option to include blockades ("❌"), which are randomly placed in the matrix except from places that would make the algorithm get stuck.

Matrix Loading and Saving:
The user can choose to load a previously saved matrix using pickle.
The user can also save a newly generated matrix to a file for future use.

Algorithms for Navigation:
The script offers two pathfinding algorithms for navigating from the top-left to the bottom-right of the matrix:
Advanced Algorithm: A two-step lookahead algorithm that evaluates and compares the sum of two consecutive cells in both rightward and downward directions to decide the next move.
Greedy Algorithm: A simpler algorithm that compares the values of the neighboring right and downward cells and moves in the direction with the larger value, unless blocked.

Visualization:
After every move, the matrix is printed, showing the current state with the visited cells marked by "⬜️". The current score and position are displayed after each step.

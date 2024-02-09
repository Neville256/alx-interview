import sys

def generate_solutions(n):
    """
    Generate all possible solutions for the N-queens problem.
    
    Args:
        n (int): The size of the chessboard (number of rows/columns).

    Returns:
        list: A list of lists representing the solutions, where each inner list
              contains the column index of the queen in each row.
    """
    solutions = []
    solve_n_queens(n, 0, [], solutions)
    return solutions

def solve_n_queens(n, row, current_solution, solutions):
    """
    Recursively solve the N-queens problem.

    Args:
        n (int): The size of the chessboard (number of rows/columns).
        row (int): The current row being considered.
        current_solution (list): The current solution being built.
        solutions (list): The list to store the valid solutions.

    Returns:
        None
    """
    if row == n:
        solutions.append(current_solution[:])  # Make a copy to avoid mutating the solution
        return
    for col in range(n):
        if is_safe(row, col, current_solution):
            current_solution.append(col)
            solve_n_queens(n, row + 1, current_solution, solutions)
            current_solution.pop()

def is_safe(row, col, current_solution):
    """
    Check if placing a queen at the given position is safe.

    Args:
        row (int): The row index to check.
        col (int): The column index to check.
        current_solution (list): The current solution being built.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for r, c in enumerate(current_solution):
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def main():
    """
    Main function to parse command-line arguments and print solutions.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 nqueens.py N")
        sys.exit(1)
    n = sys.argv[1]
    if not n.isdigit():
        print("N must be a positive integer")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = generate_solutions(n)
    for solution in solutions:
        print(solution)

if __name__ == '__main__':
    main()

def print_row_recursive(n, current_row=1):
    if current_row > n:
        return
    # Print leading spaces
    print(" " * (n - current_row), end="")
    # Print numbers for the current row
    for j in range(1, 2 * current_row):
        print(j, end=" ")
    print()  # Move to the next line
    print_row_recursive(n, current_row + 1)

# Example usage
num_lines = int(input("Enter the number of lines: "))
print_row_recursive(num_lines)

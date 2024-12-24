def alphabet_pattern_comprehension(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        
        # Use list comprehension to generate the first half of the pattern
        left_half = [chr(64 + j) for j in range(1, i + 1)]
        right_half = left_half[:-1][::-1]  # Reverse the left half (excluding the middle letter)
        
        # Join and print the full line
        print(" ".join(left_half + right_half))

# Example usage
num_lines = int(input("Enter the number of lines: "))
alphabet_pattern_comprehension(num_lines)

def fibonacci_list_comprehension(n):
    fib_sequence = [0, 1]
    [fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) for _ in range(2, n)]
    return fib_sequence[:n]

# Example usage
num_terms = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence up to {num_terms} terms: {fibonacci_list_comprehension(num_terms)}")

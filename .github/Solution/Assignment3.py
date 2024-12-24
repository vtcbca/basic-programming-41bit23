def fibonacci_iterative(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage
num_terms = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence up to {num_terms} terms: {fibonacci_iterative(num_terms)}")

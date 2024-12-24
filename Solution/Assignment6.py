def star_pattern_recursive(n, i=1):
    if i > n:
        return
    print('* ' * i)
    star_pattern_recursive(n, i + 1)

# Example usage
num_rows = int(input("Enter the number of rows: "))
star_pattern_recursive(num_rows)

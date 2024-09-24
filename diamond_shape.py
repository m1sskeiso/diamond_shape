def print_diamond(n):
    # Check if the number is odd
    if n % 2 == 0:
        return "Please provide an odd integer."

    # Print the top half of the diamond
    for i in range(1, n+1, 2):
        print(" " * ((n - i) // 2) + "*" * i)

    # Print the bottom half of the diamond
    for i in range(n-2, 0, -2):
        print(" " * ((n - i) // 2) + "*" * i)

# Example usage
n = int(input("Enter an odd integer: "))
result = print_diamond(n)
if result:
    print(result)

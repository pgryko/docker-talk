import argparse


def fibonacci(n: int):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Driver Program

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Print the first N terms of the Fibonacci sequence')
    parser.add_argument('integer', type=int, nargs='?',
                        help='Number of elements to print')
    args = parser.parse_args()
    print(fibonacci(args.integer))

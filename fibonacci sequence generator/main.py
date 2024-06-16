def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    num = int(input("Enter the number of Fibonacci numbers to generate: "))
    fib_sequence = fibonacci(num)
    print(f"Fibonacci sequence ({num} numbers): {fib_sequence}")

if __name__ == "__main__":
    main()

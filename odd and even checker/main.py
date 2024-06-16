def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    num = int(input("Enter a number: "))
    result = check_odd_even(num)
    print(f"The number {num} is {result}.")

if __name__ == "__main__":
    main()

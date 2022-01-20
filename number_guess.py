# Written by Saud Kadiri on 20th January 💛

import random

def main():
    lo = int(input("Enter the lower bound: "))
    hi = int(input("Enter the upper bound: "))

    try:
        num = random.randint(lo, hi)
    except ValueError:
        print("Invalid range")
        exit(1)

    attempts = 1
    while True:
        guess = int(input("Enter a number of your choice: "))
        if guess == num:
            print("You guessed it right!")
            break
        elif guess < num:
            print("Low")
        else:
            print("High")
        attempts += 1

    print(f"You guessed the correct number in {attempts} attempt{'s' if attempts > 1 else ''}.")


if __name__ == '__main__':
    main()

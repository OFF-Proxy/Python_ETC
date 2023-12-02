import sys
from enum import Enum
import random

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def number_generator(n):
    unique_numbers = set()

    def generator():
        for _ in range(n):
            number = Color(random.choice(list(Color))).value
            unique_numbers.add(number)
            yield number

    return generator, unique_numbers

square = lambda x: x * x

def main():
    if len(sys.argv) != 2:
        print("Usage: python exercise.py <number>")
        sys.exit(1)

    n = int(sys.argv[1])
    gen, unique_numbers = number_generator(n)

    for number in gen():
        print(f"Original number: {number}, Squared: {square(number)}")

    print(f"Unique numbers generated: {unique_numbers}")

if __name__ == "__main__":
    main()

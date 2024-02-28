"""
-------------------------------------------------------
Lab 01, Task 01
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-10"
-------------------------------------------------------
"""
# Imports
from Food import Food


# Constants


def main():
    print("Food.origins():")
    print(Food.origins())
    example_food = Food("Tomato", 0, True, 50)
    print('-'*20)
    print()
    print("Try printing Food example_food('Tomato', 0, true, 50):")
    print(str(example_food))


if __name__ == "__main__":
    main()

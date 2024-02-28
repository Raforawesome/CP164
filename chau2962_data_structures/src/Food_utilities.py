"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  Tahir Chaudhry
ID:      169052962
Email:   chau2962@mylaurier.ca
__updated__ = "2024-01-10"
-------------------------------------------------------
"""
from Food import Food


positives = ["yes", "true", "t", "y"]
# negatives = ("no", "false", "f", "n")  <-- not needed


def _parse_bool(inp: str) -> bool:  # private function
    return inp.lower() in positives


def get_food():
    """
    -------------------------------------------------------
    Creates a Food object by requesting data from a user.
    Use: source = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """
    name = input("Name: ")
    print("Origin")
    print(Food.origins())
    origin = int(input(": "))
    is_vegetarian = _parse_bool(input("Is this dish vegetarian (y/n)? "))
    calories = int(input("Enter number of calories: "))
    food = Food(name, origin, is_vegetarian, calories)
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a Food object from a line of string data.
    Use: source = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    name, origin, is_vegetarian, calories = line.split("|")
    is_vegetarian = _parse_bool(is_vegetarian)
    calories = int(calories)
    origin = int(origin)
    food = Food(name, origin, is_vegetarian, calories)
    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    foods = []
    line = file_variable.readline()
    while line != "":
        foods.append(read_food(line))
        line = file_variable.readline()
    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of Food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file variable)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    for food in foods:
        food.write(file_variable)
    return None


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian Food objects.
    foods is unchanged.
    Use: v_foods = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    veggies = [f for f in foods if f.is_vegetarian]
    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of Food objects by origin.
    foods is unchanged.
    Use: o_foods = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    origins = [f for f in foods if f.origin == origin]
    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    total = sum(map(lambda f: f.calories, foods))
    count = len(foods)
    avg = total / count
    return int(avg)


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of Foods objects.
    foods is unchanged.
    Use: by_origin = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    filtered = list(map(lambda f: f.calories, filter(
        lambda f: f.origin == origin, foods)))
    total = sum(filtered)
    count = len(filtered)
    avg = total / count
    return int(avg)


# Constants
LEN1 = 35
LEN2 = 12
LEN3 = 10
LEN4 = 8
HEAD1 = '-' * LEN1
HEAD2 = '-' * LEN2
HEAD3 = '-' * LEN3
HEAD4 = '-' * LEN4
LINE1 = f"{'Food':<{LEN1}} {'Origin':<{LEN2}} {'Vegetarian':<{LEN3}} {'Calories':<{LEN4}}"
LINE2 = f"{HEAD1:<{LEN1}} {HEAD2:<{LEN2}} {HEAD3:<{LEN3}} {HEAD4:<{LEN4}}"


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of Food objects, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    s_foods = sorted(foods)
    print(LINE1)
    print(LINE2)
    for food in s_foods:
        origin_name = Food.ORIGIN[food.origin]
        line = f"{food.name:<{LEN1}} {origin_name:<{LEN2}} {str(food.is_vegetarian):>{LEN3}} {food.calories:>{LEN4}}"
        print(line)
    return None


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for Food objects that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))
    result = [
        food for food in foods if
        (food.origin == origin or origin == -1) and
        (food.calories <= max_cals or max_cals == 0) and
        (food.is_vegetarian is True or is_veg is False)
    ]
    return result

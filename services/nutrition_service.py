from utils.food_database import FOOD_DATABASE


def get_food_information(food_name):

    food_name = food_name.lower()

    for key in FOOD_DATABASE:

        if key in food_name:

            return FOOD_DATABASE[key]

    return None
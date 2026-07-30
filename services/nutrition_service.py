from utils.nutrition_database import FOOD_DATABASE


def get_nutrition(food_name):

    food_name = food_name.lower()

    for item in FOOD_DATABASE:

        if item in food_name:
            return FOOD_DATABASE[item]

    return {
        "Calories": "Unknown",
        "Protein": "Unknown",
        "Fat": "Unknown",
        "Carbohydrates": "Unknown",
        "Health Score": 0,
        "Alternative": "Unknown"
    }
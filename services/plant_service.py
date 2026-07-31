from utils.plant_database import PLANT_DATABASE


def diagnose_plant(label):
    """
    Find plant information from the local database.
    """

    label = label.lower()

    for plant in PLANT_DATABASE:

        if plant in label:

            return PLANT_DATABASE[plant]

    return None
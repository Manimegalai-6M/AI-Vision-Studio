from utils.fashion_database import FASHION_DATABASE


def get_fashion_advice(label):
    """
    Search the fashion database using the predicted clothing label.
    """

    label = label.lower()

    for item in FASHION_DATABASE:

        if item in label:
            return FASHION_DATABASE[item]

    return None
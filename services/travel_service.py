from utils.travel_database import TRAVEL_DATABASE


def get_travel_information(label):

    label = label.lower()

    for place in TRAVEL_DATABASE:

        if place in label:
            return TRAVEL_DATABASE[place]

    return None
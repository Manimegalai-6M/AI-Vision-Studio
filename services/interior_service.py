from utils.interior_database import INTERIOR_DATABASE


def get_room_information(label):

    label = label.lower()

    for room in INTERIOR_DATABASE:

        if room in label:

            return INTERIOR_DATABASE[room]

    return None
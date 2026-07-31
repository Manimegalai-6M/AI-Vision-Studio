from utils.cultural_database import CULTURAL_DATABASE

def get_cultural_info(label):

    label = label.lower()

    for item in CULTURAL_DATABASE:

        if item in label:
            return CULTURAL_DATABASE[item]

    return None
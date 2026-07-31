from utils.recycle_database import RECYCLE_DATABASE


def get_recycling_info(label):
    """
    Search the recycling database using the predicted label.
    """

    label = label.lower()

    for item in RECYCLE_DATABASE:

        if item in label:
            return RECYCLE_DATABASE[item]

    return None
from utils.timeline_database import TIMELINE_DATABASE


def get_timeline(label):

    label = label.lower()

    for key in TIMELINE_DATABASE:

        if key in label:
            return TIMELINE_DATABASE[key]

    return None
from utils.historical_database import HISTORICAL_DATABASE

def get_historical_info(label):
    label = label.lower()

    for item in HISTORICAL_DATABASE:
        if item in label:
            return HISTORICAL_DATABASE[item]

    return None
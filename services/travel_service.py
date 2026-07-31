from utils.travel_database import TRAVEL_DATABASE

# Different names that mean the same place
PLACE_ALIASES = {
    "masjid": "mosque",
    "cathedral": "church",
    "chapel": "church",
    "fortress": "fort",
    "palatial building": "palace"
}


def get_travel_information(label):

    if not label:
        return None

    # Convert to lowercase
    label = label.lower()

    # Example:
    # "Mosque, Masjid"
    # becomes
    # "mosque"
    label = label.split(",")[0].strip()

    # Replace aliases
    label = PLACE_ALIASES.get(label, label)

    # Exact match
    if label in TRAVEL_DATABASE:
        return TRAVEL_DATABASE[label]

    # Partial match
    for place in TRAVEL_DATABASE:
        if place in label:
            return TRAVEL_DATABASE[place]

    return None
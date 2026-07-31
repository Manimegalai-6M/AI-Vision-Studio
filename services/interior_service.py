from utils.interior_database import INTERIOR_DATABASE

# Different names that mean the same room
ROOM_ALIASES = {
    "home theatre": "home theater",
    "movie theater": "home theater",
    "cinema": "home theater",
    "hall": "living room",
    "lounge": "living room",
    "study": "office",
    "workspace": "office",
    "washroom": "bathroom",
    "restroom": "bathroom",
}


def get_room_information(label):
    """
    Returns room information from the local database.
    """

    if not label:
        return None

    # Convert to lowercase
    label = label.lower()

    # Example:
    # "Home Theater, Home Theatre"
    # becomes
    # "home theater"
    label = label.split(",")[0].strip()

    # Replace aliases
    label = ROOM_ALIASES.get(label, label)

    # Exact match
    if label in INTERIOR_DATABASE:
        return INTERIOR_DATABASE[label]

    # Partial match
    for room in INTERIOR_DATABASE:
        if room in label:
            return INTERIOR_DATABASE[room]

    return None
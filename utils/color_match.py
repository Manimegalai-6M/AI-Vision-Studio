MATCHING_COLORS = {

    "Blue": ["White", "Black", "Gray"],

    "Black": ["White", "Red", "Gray"],

    "White": ["Blue", "Black", "Brown"],

    "Red": ["Black", "White", "Gray"],

    "Green": ["White", "Black", "Beige"],

    "Gray": ["Blue", "Black", "White"]

}


def get_matching_colors(color):
    """
    Return recommended matching colors.
    """

    return MATCHING_COLORS.get(color, [])
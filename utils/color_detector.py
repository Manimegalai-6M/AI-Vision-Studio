import numpy as np


def detect_dominant_color(image):
    """
    Detect the dominant color of the uploaded image.
    """

    img = np.array(image)

    avg = img.mean(axis=(0, 1))

    r, g, b = avg

    if r > 200 and g > 200 and b > 200:
        return "White"

    if r < 60 and g < 60 and b < 60:
        return "Black"

    if r > g and r > b:
        return "Red"

    if g > r and g > b:
        return "Green"

    if b > r and b > g:
        return "Blue"

    return "Gray"
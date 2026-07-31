import numpy as np


def detect_room_color(image):

    img = np.array(image)

    r, g, b = img.mean(axis=(0, 1))

    if r > 200 and g > 200 and b > 200:
        return "White"

    if r < 60 and g < 60 and b < 60:
        return "Black"

    if r > b and r > g:
        return "Brown"

    if g > r and g > b:
        return "Green"

    if b > r and b > g:
        return "Blue"

    return "Gray"
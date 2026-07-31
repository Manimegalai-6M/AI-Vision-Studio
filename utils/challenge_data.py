import random

CHALLENGE_OBJECTS = [
    "person",
    "chair",
    "bottle",
    "book",
    "cell phone",
    "laptop",
    "dog",
    "cat",
    "car",
    "bicycle",
    "apple",
    "banana",
    "cup",
    "backpack",
    "clock"
]

def generate_challenge(size=5):
    return random.sample(CHALLENGE_OBJECTS, size)
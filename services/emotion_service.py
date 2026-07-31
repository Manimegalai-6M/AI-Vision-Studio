SCENE_TO_EMOTION = {

    "volcano": "Fear",

    "fire": "Fear",

    "forest": "Peaceful",

    "mountain": "Calm",

    "beach": "Relaxed",

    "ocean": "Calm",

    "garden": "Happy",

    "flower": "Happy",

    "stadium": "Excited",

    "concert": "Excited",

    "rain": "Sad",

    "snow": "Peaceful",

    "sunset": "Calm"

}


def get_emotion(label):

    label = label.lower()

    for key in SCENE_TO_EMOTION:

        if key in label:

            return SCENE_TO_EMOTION[key]

    return "Neutral"
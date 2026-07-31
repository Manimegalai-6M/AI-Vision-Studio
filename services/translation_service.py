"""
translation_service.py

Translate prediction labels into multiple languages.
"""

TRANSLATIONS = {
    "Tamil": {
        "cat": "பூனை",
        "dog": "நாய்",
        "car": "கார்",
        "person": "நபர்",
        "bird": "பறவை",
        "bicycle": "மிதிவண்டி",
        "bus": "பேருந்து",
        "truck": "லாரி",
        "motorcycle": "மோட்டார் சைக்கிள்",
        "airplane": "விமானம்",
        "train": "ரயில்",
        "boat": "படகு"
    },

    "Hindi": {
        "cat": "बिल्ली",
        "dog": "कुत्ता",
        "car": "कार",
        "person": "व्यक्ति",
        "bird": "पक्षी",
        "bicycle": "साइकिल",
        "bus": "बस",
        "truck": "ट्रक",
        "motorcycle": "मोटरसाइकिल",
        "airplane": "हवाई जहाज",
        "train": "रेल",
        "boat": "नाव"
    },

    "French": {
        "cat": "Chat",
        "dog": "Chien",
        "car": "Voiture",
        "person": "Personne",
        "bird": "Oiseau",
        "bicycle": "Vélo",
        "bus": "Bus",
        "truck": "Camion",
        "motorcycle": "Moto",
        "airplane": "Avion",
        "train": "Train",
        "boat": "Bateau"
    },

    "Japanese": {
        "cat": "猫",
        "dog": "犬",
        "car": "車",
        "person": "人",
        "bird": "鳥",
        "bicycle": "自転車",
        "bus": "バス",
        "truck": "トラック",
        "motorcycle": "オートバイ",
        "airplane": "飛行機",
        "train": "電車",
        "boat": "ボート"
    }
}


def translate_predictions(predictions, language):
    """
    Translate prediction labels.

    Parameters
    ----------
    predictions : list
        Example:
        [
            {"label": "cat", "score": 0.97},
            {"label": "dog", "score": 0.02}
        ]

    language : str
        English, Tamil, Hindi, French, Japanese

    Returns
    -------
    list
        Same prediction list with translated labels.
    """

    if language == "English":
        return predictions

    dictionary = TRANSLATIONS.get(language, {})

    translated_predictions = []

    for prediction in predictions:

        item = prediction.copy()

        label = item["label"].lower()

        item["label"] = dictionary.get(label, prediction["label"])

        translated_predictions.append(item)

    return translated_predictions
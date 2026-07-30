from utils.translator import translate_label

def translate_predictions(predictions, language):

    translated = []

    for item in predictions:

        translated.append({

            "label": translate_label(
                item["label"],
                language
            ),

            "score": item["score"]

        })

    return translated
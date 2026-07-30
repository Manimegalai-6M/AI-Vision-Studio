from deep_translator import GoogleTranslator

SUPPORTED_LANGUAGES = {
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Japanese": "ja"
}

def translate_label(text):
    """
    Translate a prediction label into multiple languages.
    """

    translations = {}

    for language, code in SUPPORTED_LANGUAGES.items():

        try:
            translated = GoogleTranslator(
                source="auto",
                target=code
            ).translate(text)

            translations[language] = translated

        except Exception:
            translations[language] = "Translation Failed"

    return translations
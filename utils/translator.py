from deep_translator import GoogleTranslator

LANGUAGE_CODES = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Japanese": "ja"
}

def translate_label(text, language):
    if language == "English":
        return text

    try:
        return GoogleTranslator(
            source="auto",
            target=LANGUAGE_CODES[language]
        ).translate(text)
    except:
        return text
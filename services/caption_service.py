from models.caption_model import load_caption_model


def generate_caption(image):
    """
    Generate a caption for the uploaded image.
    """

    model = load_caption_model()

    result = model(image)

    return result[0]["generated_text"]
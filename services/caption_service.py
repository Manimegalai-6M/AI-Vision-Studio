import torch

from models.caption_model import load_caption_model


def generate_caption(image):

    processor, model = load_caption_model()


    inputs = processor(
        images=image,
        return_tensors="pt"
    )


    output = model.generate(
        **inputs,
        max_length=50
    )


    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )


    return caption
    return caption
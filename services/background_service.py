from rembg import remove
from PIL import Image
from io import BytesIO


def remove_background(image: Image.Image):
    """
    Removes the background from a PIL image.

    Returns:
        output_image (PIL.Image)
    """

    buffer = BytesIO()

    image.save(buffer, format="PNG")

    output = remove(buffer.getvalue())

    result = Image.open(BytesIO(output)).convert("RGBA")

    return result
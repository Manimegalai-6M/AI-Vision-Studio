from PIL import Image
import math


def get_image_info(image: Image.Image, uploaded_file):
    """
    Returns image information.
    """

    width, height = image.size

    gcd = math.gcd(width, height)
    aspect_ratio = f"{width//gcd}:{height//gcd}"

    return {
        "Width": width,
        "Height": height,
        "Format": image.format if image.format else "Unknown",
        "Mode": image.mode,
        "File Size (KB)": round(uploaded_file.size / 1024, 2),
        "Aspect Ratio": aspect_ratio
    }
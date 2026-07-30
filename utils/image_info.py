from PIL import Image

def get_image_info(image: Image.Image, uploaded_file):
    """
    Returns image information.
    """

    width, height = image.size

    return {
        "Width": width,
        "Height": height,
        "Format": image.format if image.format else "Unknown",
        "Mode": image.mode,
        "File Size (KB)": round(uploaded_file.size / 1024, 2)
    }
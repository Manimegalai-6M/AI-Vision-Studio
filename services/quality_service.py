import cv2
import numpy as np


def analyze_quality(image):
    """
    Analyze image quality.

    Returns:
        Dictionary containing blur,
        brightness,
        contrast,
        sharpness,
        overall score.
    """

    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Blur (Variance of Laplacian)
    blur = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Brightness
    brightness = np.mean(gray)

    # Contrast
    contrast = gray.std()

    # Sharpness
    sharpness = blur

    # Overall score (0-100)

    blur_score = min(100, blur / 5)

    brightness_score = 100 - abs(brightness - 128)

    brightness_score = max(0, brightness_score)

    contrast_score = min(100, contrast * 2)

    overall = (
        blur_score +
        brightness_score +
        contrast_score
    ) / 3

    return {
        "Blur": round(blur, 2),
        "Brightness": round(brightness, 2),
        "Contrast": round(contrast, 2),
        "Sharpness": round(sharpness, 2),
        "Overall": round(overall, 2)
    }
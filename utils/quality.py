import cv2
import numpy as np
from PIL import Image


def analyze_image_quality(image: Image.Image):
    """
    Analyze image quality metrics:
    - Blur
    - Brightness
    - Contrast
    - Sharpness
    """

    img = np.array(image.convert("RGB"))
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Blur (Variance of Laplacian)
    blur = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Brightness
    brightness = np.mean(gray)

    # Contrast
    contrast = np.std(gray)

    # Sharpness (Gradient Magnitude)
    gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
    gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

    sharpness = np.mean(np.sqrt(gx**2 + gy**2))

    # Overall Score (0-100)
    score = (
        min(blur / 5, 25)
        + min(brightness / 255 * 25, 25)
        + min(contrast / 64 * 25, 25)
        + min(sharpness / 10 * 25, 25)
    )

    score = round(score, 2)

    if score >= 85:
        status = "🌟 Excellent"

    elif score >= 70:
        status = "✅ Good"

    elif score >= 50:
        status = "🟡 Average"

    else:
        status = "🔴 Poor"

    return {
        "Blur": round(blur, 2),
        "Brightness": round(brightness, 2),
        "Contrast": round(contrast, 2),
        "Sharpness": round(sharpness, 2),
        "Score": score,
        "Status": status
    }
"""
utils/similarity.py

Utility functions for comparing two images.
"""

import numpy as np
import cv2

from PIL import Image
from skimage.metrics import structural_similarity as ssim


# ---------------------------------------------------
# Convert PIL Image to OpenCV
# ---------------------------------------------------

def pil_to_cv(image: Image.Image):
    """
    Convert PIL image to OpenCV (NumPy) format.
    """
    image = image.convert("RGB")
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)


# ---------------------------------------------------
# Resize Images
# ---------------------------------------------------

def resize_images(img1, img2, size=(256, 256)):
    """
    Resize both images to the same size.
    """
    img1 = cv2.resize(img1, size)
    img2 = cv2.resize(img2, size)

    return img1, img2


# ---------------------------------------------------
# Histogram Similarity
# ---------------------------------------------------

def histogram_similarity(img1, img2):
    """
    Compare color histograms.
    Returns similarity between 0 and 100.
    """

    hist1 = cv2.calcHist(
        [img1],
        [0, 1, 2],
        None,
        [8, 8, 8],
        [0, 256, 0, 256, 0, 256]
    )

    hist2 = cv2.calcHist(
        [img2],
        [0, 1, 2],
        None,
        [8, 8, 8],
        [0, 256, 0, 256, 0, 256]
    )

    cv2.normalize(hist1, hist1)
    cv2.normalize(hist2, hist2)

    similarity = cv2.compareHist(
        hist1,
        hist2,
        cv2.HISTCMP_CORREL
    )

    similarity = max(0.0, similarity)

    return round(similarity * 100, 2)


# ---------------------------------------------------
# Structural Similarity (SSIM)
# ---------------------------------------------------

def structural_similarity_score(img1, img2):
    """
    Calculate SSIM score.
    """

    gray1 = cv2.cvtColor(
        img1,
        cv2.COLOR_BGR2GRAY
    )

    gray2 = cv2.cvtColor(
        img2,
        cv2.COLOR_BGR2GRAY
    )

    score = ssim(gray1, gray2)

    return round(score * 100, 2)


# ---------------------------------------------------
# Average Similarity
# ---------------------------------------------------

def average_similarity(hist_score, ssim_score):
    """
    Average histogram and SSIM scores.
    """

    return round(
        (hist_score + ssim_score) / 2,
        2
    )


# ---------------------------------------------------
# Compare Image Size
# ---------------------------------------------------

def compare_size(image1: Image.Image, image2: Image.Image):
    """
    Compare image dimensions.
    """

    return {
        "image1": {
            "width": image1.width,
            "height": image1.height
        },
        "image2": {
            "width": image2.width,
            "height": image2.height
        }
    }


# ---------------------------------------------------
# Compare Formats
# ---------------------------------------------------

def compare_format(image1: Image.Image, image2: Image.Image):
    """
    Compare image formats.
    """

    return {
        "image1": image1.format,
        "image2": image2.format
    }


# ---------------------------------------------------
# Main Comparison Function
# ---------------------------------------------------

def compare_images(image1: Image.Image, image2: Image.Image):
    """
    Compare two PIL images.
    """

    cv_img1 = pil_to_cv(image1)
    cv_img2 = pil_to_cv(image2)

    cv_img1, cv_img2 = resize_images(
        cv_img1,
        cv_img2
    )

    hist = histogram_similarity(
        cv_img1,
        cv_img2
    )

    ssim_score = structural_similarity_score(
        cv_img1,
        cv_img2
    )

    avg = average_similarity(
        hist,
        ssim_score
    )

    return {
        "histogram": hist,
        "ssim": ssim_score,
        "average": avg
    }
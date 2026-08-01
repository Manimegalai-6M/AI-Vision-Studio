"""
services/comparison_service.py

Main service for comparing two images.
"""

from utils.similarity import compare_images

# Reuse your existing services
from services.classifier_service import classify_image
from utils.image_info import get_image_info


# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

def get_prediction(image):
    """
    Returns the top prediction.
    """

    predictions = classify_image(image)

    if not predictions:
        return {
            "label": "Unknown",
            "confidence": 0
        }

    best = predictions[0]

    return {
        "label": best["label"],
        "confidence": round(best["score"] * 100, 2)
    }


# ---------------------------------------------------
# AI Summary
# ---------------------------------------------------

def generate_summary(pred1, pred2, similarity):

    label1 = pred1["label"]
    label2 = pred2["label"]

    confidence1 = pred1["confidence"]
    confidence2 = pred2["confidence"]

    if label1.lower() == label2.lower():

        object_text = (
            f"Both images are predicted as '{label1}'."
        )

    else:

        object_text = (
            f"Image 1 contains '{label1}', "
            f"while Image 2 contains '{label2}'."
        )

    if similarity >= 90:

        sim_text = (
            "The images are extremely similar."
        )

    elif similarity >= 75:

        sim_text = (
            "The images are highly similar."
        )

    elif similarity >= 50:

        sim_text = (
            "The images are moderately similar."
        )

    else:

        sim_text = (
            "The images are visually different."
        )

    summary = f"""
Image Comparison Summary

• {object_text}

• Prediction confidence:
  Image 1 : {confidence1:.2f}%
  Image 2 : {confidence2:.2f}%

• Overall similarity:
  {similarity:.2f}%

• {sim_text}
"""

    return summary.strip()


# ---------------------------------------------------
# Complete Comparison
# ---------------------------------------------------

def compare_image_data(image1, image2, uploaded1, uploaded2):

    prediction1 = get_prediction(image1)
    prediction2 = get_prediction(image2)

    info1 = get_image_info(image1, uploaded1)
    info2 = get_image_info(image2, uploaded2)

    similarity = compare_images(image1, image2)

    summary = generate_summary(
        prediction1,
        prediction2,
        similarity["average"]
    )

    return {

        "prediction1": prediction1,
        "prediction2": prediction2,

        "info1": info1,
        "info2": info2,

        "similarity": similarity,

        "summary": summary

    }
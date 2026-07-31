from models.yolo_model import load_yolo
from PIL import Image
import numpy as np
import cv2


def detect_objects(image):

    model = load_yolo()

    img = np.array(image)

    results = model(img)

    result = results[0]

    annotated = result.plot()

    annotated = cv2.cvtColor(
        annotated,
        cv2.COLOR_BGR2RGB
    )

    object_counts = {}

    for box in result.boxes:

        cls = int(box.cls[0])

        name = model.names[cls]

        object_counts[name] = (
            object_counts.get(name, 0) + 1
        )

    total = sum(object_counts.values())

    return (
        Image.fromarray(annotated),
        object_counts,
        total
    )
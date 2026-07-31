import cv2
import numpy as np

CASCADE_PATH = "weights/haarcascade_frontalface_default.xml"

face_detector = cv2.CascadeClassifier(CASCADE_PATH)


def detect_faces(image):
    """
    Detect faces in a PIL image.

    Returns:
        annotated_image,
        face_count
    """

    image_np = np.array(image)

    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40)
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(
            image_bgr,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

    result = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    return result, len(faces)
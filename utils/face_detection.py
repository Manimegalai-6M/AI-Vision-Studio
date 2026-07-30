import cv2
import mediapipe as mp
import numpy as np
from PIL import Image

# Load MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


def detect_faces(image):
    """
    Detect faces and draw bounding boxes.

    Parameters:
        image (PIL.Image)

    Returns:
        output_image (PIL.Image)
        face_count (int)
    """

    # Convert PIL Image to OpenCV
    image_np = np.array(image)
    image_rgb = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)

    face_count = 0

    with mp_face_detection.FaceDetection(
        model_selection=1,
        min_detection_confidence=0.5
    ) as detector:

        results = detector.process(image_rgb)

        if results.detections:

            face_count = len(results.detections)

            for detection in results.detections:

                bbox = detection.location_data.relative_bounding_box

                h, w, _ = image_rgb.shape

                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                width = int(bbox.width * w)
                height = int(bbox.height * h)

                cv2.rectangle(
                    image_np,
                    (x, y),
                    (x + width, y + height),
                    (0, 255, 0),
                    3
                )

    output = Image.fromarray(image_np)

    return output, face_count
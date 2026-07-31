from transformers import pipeline

emotion_classifier = pipeline(
    "image-classification",
    model="microsoft/resnet-50"
)

def predict_scene(image):

    return emotion_classifier(image)
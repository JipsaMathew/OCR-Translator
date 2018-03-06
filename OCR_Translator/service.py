import io
import os
from google.cloud import vision
from google.cloud.vision import types
# from google.cloud import storage
from google.cloud import translate


class Service:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"
    ] = r'C:\Users\Jipsa\Documents\UTTyler-Spring 2018\COSC 5399\api_key.json'


def detect_text():
    """vision api text detection feature"""

    vision_client = vision.ImageAnnotatorClient()
    file_name = r'C:\Users\Jipsa\Documents\UTTyler-Spring 2018\COSC 5399\cosc5399\OCR_Translator\atlanta.jpg'
    with io.open(file_name,
                 'rb') as image_file:
        content = image_file.read()

        image = types.Image(content=content)

    response = vision_client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        return text.description


# Translate api


def main():
    """main method for service class"""

    msg = detect_text()  # detected text from the image
    print(msg)


# calling main method
main()

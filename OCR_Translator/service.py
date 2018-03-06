import io
import os
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import translate


class Service:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"
    ] = r'C:\Users\Jipsa\Documents\UTTyler-Spring 2018\COSC 5399\api_key.json'


def detect_text(path):
    """vision api text detection feature"""

    vision_client = vision.ImageAnnotatorClient()
    # file_name = r'C:\Users\Jipsa\Documents\UTTyler-Spring 2018\COSC 5399\cosc5399\OCR_Translator\atlanta.jpg'
    file_name = path
    with io.open(file_name,
                 'rb') as image_file:
        content = image_file.read()

        image = types.Image(content=content)

    response = vision_client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        return text.description


# Translate api

def translate_text(msg, lang):
    # Instantiates a client
    translate_client = translate.Client()
    text = msg
    # The target language
    target = lang

    # Translates some text into target
    result = translate_client.translate(
        text,
        target_language=target)

    #print(u'Text: {}'.format(text))
    return result['translatedText']

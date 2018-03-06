from django.shortcuts import render

from OCR_Translator.service import detect_text, translate_text


# Create your views here.

def index(request):
    return render(request, 'OCR_Translator/index.html')


def main():
    """main method for service class"""
    path = r'C:\Users\Jipsa\Documents\UTTyler-Spring 2018\COSC 5399\cosc5399\OCR_Translator\atlanta.jpg'
    msg = detect_text(path)  # detected text from the image
    print(msg)

    lang = 'de'
    t_msg = translate_text(msg, lang)
    print(t_msg)


# calling main method

main()

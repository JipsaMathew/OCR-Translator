from django.shortcuts import render
import os
from OCR_Translator.service import detect_text, translate_text
from .forms import SelectForm


# Create your views here.


def get_form_data(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SelectForm(request.POST, request.FILES) 
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            t_lang = form.cleaned_data['lang']   
            # file contains the image. Django saves uploaded images in request.FILE
            file = request.FILES['ocr_image']
            name = file.name
            # print(name)
            storage_path = r'C:\Users\Jipsa\Documents\UTTyler-Spring 2018\COSC 5399\Images'
            path = os.path.join(storage_path, name)
            print(path)
            msg = detect_text(path)  # detected text from the image
            print(msg)

            t_msg = translate_text(msg, t_lang)

            print(t_msg)

        # if a GET (or any other method) we'll create a blank form
    else:
        form = SelectForm()

    return render(request, 'OCR_Translator/name.html', {'form': form})

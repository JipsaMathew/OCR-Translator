from django import forms

# form class for creating a form rendered via name.html

LANG_CHOICES = (
    ('ms', 'Bahasa Melayu'), ('hy', 'Armenian'), ('zh', 'Chinese'), ('cz', 'Czech'), ('da', 'Danish'),
    ('nl', 'Dutch'),
    ('en', 'English'), ('eo', 'Esperanto'), ('fi', 'Finnish'),
    ('fr', 'French'), ('ka', 'Georgian'), ('de', 'German'), ('el', 'Greek'), ('it', 'Italian'),
    ('ja', 'Japanese'), ('ko', 'Korean'), ('ku', 'Kurdish'), ('fa', 'Persian'), ('pl', 'Polish'),
    ('pt', 'Portuguese'),
    ('ro', 'Romanian'), ('ru', 'Russian'), ('es', 'Spanish'),
    ('sv', 'Swedish'), ('tr', 'Turkish'), ('ur', 'Urdu'))


class SelectForm(forms.Form):
    lang = forms.ChoiceField(label='Choose Language', choices=LANG_CHOICES)
    ocr_image = forms.ImageField(label='Upload your Image')

# class ImageUploadForm(forms.Form):
# image = forms.ImageField(label='Upload your Image')

:# Optical Character Recognizer (OCR) and Translator

# Overview
This project implements an Optical Character Recognizer (OCR) and Translator which recognizes words in an image and translates it to desired language. This project is being developed as required by COSC 5399.
Functionality
1)	The OCR Translator takes input as an image stored in the device.
2)	 User chooses the output language.
3)	 The text/words/blocks of words are recognized by the application and the translated text is displayed to the user.

# Technical Specifications
Programming Language: Python 3.6.4
Web Framework: Django 2.0.2
IDE: Jetbrains Pycharm
Version Control: Git
APIs:
1. Google Cloud Vision API
2. Google Translation API

# Milestones
I.	Optical Character Recognition: 
Detects and extracts text within an image, with support for a broad range of languages, along with support for automatic language identification. This is done with the Optical Character Recognition feature of Google’s Cloud Vision REST api.

II.	Translating Output Text: 
The extracted text is send to Google Translate REST api as a JSON request and the api sends the translated text as response which is displayed to the user.
The Translation API's recognition engine auto detects and supports a wide variety of languages for the Phrase-Based Machine Translation (PBMT) and Neural Machine Translation (NMT) models. These languages are specified within a recognition request using language code parameters. Most language code parameters conform to ISO-639-1 identifier.

# Reference
1.	https://cloud.google.com/
2.	https://docs.djangoproject.com/en/2.0/
3.  https://en.wikipedia.org/wiki/ISO_639-1


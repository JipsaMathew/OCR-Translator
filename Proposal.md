# Optical Character Recognizer (OCR) and Translator

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

1. Setting up Project Environment:
The project requires Google Cloud Machine Learning APIs. These apis are RESTful in architectural style and sends and receives data in JSON format. How Google Cloud Platform authorizes these API access is described here:

GCP client libraries use a strategy called Application Default Credentials (ADC) to find the application's credentials. When the code uses a client library, the strategy checks for your credentials in the following order:

    1. ADC checks to see if the environment variable GOOGLE_APPLICATION_CREDENTIALS is set.
    2. If the variable is set, ADC uses the service account file that the variable points to.
    3. When the application is deployed in cloud (Google Cloud Platform), ADC uses the default service account that App Engine, and    Cloud Functions provide, for applications that run on those services.

2.	Optical Character Recognition: 
Detects and extracts text within an image, with support for a broad range of languages, along with support for automatic language identification. This is done with the Optical Character Recognition feature of Google’s Cloud Vision REST api.
The input image is sent to 
3.	Translating Output Text: 
The extracted text is send to Google Translate REST api as a JSON request and the api sends the translated text as response which is displayed to the user.
The Translation API's recognition engine auto detects and supports a wide variety of languages for the Phrase-Based Machine Translation (PBMT) and Neural Machine Translation (NMT) models. These languages are specified within a recognition request using language code parameters. Most language code parameters conform to ISO-639-1 identifier.

# Reference
1.	https://cloud.google.com/
2.	https://docs.djangoproject.com/en/2.0/
3.  https://en.wikipedia.org/wiki/ISO_639-1


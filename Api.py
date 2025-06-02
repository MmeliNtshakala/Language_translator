# Importing the necessary library for translation
from googletrans import Translator
import json

translator = Translator()

def translate_to_isizulu(massage):
    try:
        translation = translator.translate(massage, src='en', dest='zu')
        responseJson = {
            "input_text": massage,
            "translation_of _text": translation.text,
        }
        return json.dumps(responseJson, indent=4)
    except:
        return json.dumps({"error": "Translation failed"}, indent=4)

"""
    Now testing and calling the function to see the functionality
    This is us taking depth 
"""

english_text = "take me"
zulu_translation = translate_to_isizulu(english_text)
print(f"English: {english_text} \n Zulu: {zulu_translation}")
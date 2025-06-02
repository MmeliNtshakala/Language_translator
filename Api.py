# Importing the necessary library for translation
from googletrans import Translator

translator = Translator()

def translate_to_isizulu(massage):
    translation = translator.translate(massage, src='en', dest='zu')
    return translation.text

"""
    Now testing and calling the function to see the functionality
    This is us taking depth 
"""

english_text = "take me"
zulu_translation = translate_to_isizulu(english_text)
print(f"English: {english_text} \n Zulu: {zulu_translation}")
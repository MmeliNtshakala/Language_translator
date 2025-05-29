import googletrans import Translator

translator = Translator()

def zulu_translate(massage):
    translation = translator.translate(massage, src='en', dest='zu')
    return translation.text

"""
    Now testing and calling the function to see the functionality
    This is us taking depth 
"""

english_text = "take the table"
zulu_translation = zulu_translate(english_text)
print(f"English: {english_text} \n Zulu: {zulu_translation}")
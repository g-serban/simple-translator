# translator
from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('sentences.txt', mode='r') as file:
        text = file.read()
        translation = translator.translate(text)
        with open('sentences.txt', mode='w', encoding="utf-8") as my_file:
            my_file.write(translation)  
except FileNotFoundError:
    print('check the file path')

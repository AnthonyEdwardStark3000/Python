from translate import Translator

translator = Translator(to_lang='ja')
try:
    with open('File I-O/exercise.txt', mode='r') as my_file:
        data = my_file.read()
        new_data = translator.translate(data)
        print(new_data)

except FileNotFoundError as not_found:
    print(
        f'check the path entered as I have encountered an {not_found} exception')

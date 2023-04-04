from translate import Translator

translator = Translator(to_lang='ja')
'''translation = translator.translate('This is a pen')
print(translation)'''

try:
    with open('file2be_translated.txt', mode='r') as my_file:
        print(my_file.read())
        my_file.seek(0)
        be_translated = my_file.read()
        translation = translator.translate(be_translated)
        print(translation)
        try:
            with open('text-ja.txt', mode='w', encoding='utf-8') as my_file2:
                my_file2.write(translation)
        except IOError as err:
            print('it\'s not writable')
        except UnicodeEncodeError as err:
            print('cannot write those characters.')
except FileNotFoundError as err:
    print('check your file path.')

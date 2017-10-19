import os
#import string

russian_lowercase = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
russian_uppercase = list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
alphabet_length = len(russian_lowercase)

key = 'sFk25bHSgh'
#key = 7
if not isinstance(key, int):
    tmp_key = 0
    for char in key:
        tmp_key += ord(char)
    key = tmp_key

coded_text = ''

text_path = os.path.join('./texts', 'got2.txt')
file = open(text_path, 'r')
read_text = file.read()

for letter in read_text:
    if russian_lowercase.__contains__(letter):
        real_index = russian_lowercase.index(letter)
        coded_index = (real_index + key) % alphabet_length
        coded_text += russian_lowercase.__getitem__(coded_index)
    else:
        if russian_uppercase.__contains__(letter):
            real_index = russian_uppercase.index(letter)
            coded_index = (real_index + key) % alphabet_length
            coded_text += russian_uppercase.__getitem__(coded_index)
        else:
            coded_text += letter

file.close()

text_coded_path = os.path.join('./texts', 'got2_coded.txt')
res_file = open(text_coded_path, 'w+')

res_file.write(coded_text)
res_file.close()
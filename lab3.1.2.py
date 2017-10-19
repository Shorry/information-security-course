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

decoded_text = ''

text_path = os.path.join('./texts', 'got2_coded.txt')
file = open(text_path, 'r')
read_text = file.read()

for letter in read_text:
    if russian_lowercase.__contains__(letter):
        coded_index = russian_lowercase.index(letter)
        decoded_index = (coded_index - key + alphabet_length) % alphabet_length
        decoded_text += russian_lowercase.__getitem__(decoded_index)
    else:
        if russian_uppercase.__contains__(letter):
            coded_index = russian_uppercase.index(letter)
            decoded_index = (coded_index - key + alphabet_length) % alphabet_length
            decoded_text += russian_uppercase.__getitem__(decoded_index)
        else:
            decoded_text += letter

file.close()

text_decoded_path = os.path.join('./texts', 'got2_decoded.txt')
res_file = open(text_decoded_path, 'w+')

res_file.write(decoded_text)
res_file.close()
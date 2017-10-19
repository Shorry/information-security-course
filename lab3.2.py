# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 15:53:59 2017

@author: Anna
"""
import os
import operator

russian_lowercase = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
russian_uppercase = list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
alphabet_length = len(russian_lowercase)

def teach_function():
    prob_dict = dict((letter, 0) for letter in russian_lowercase)
    text_path = os.path.join('./texts', 'got2.txt')
    file = open(text_path, 'r')
    read_text = file.read()
    text_length = len(read_text)
    for letter in read_text:
        if russian_lowercase.__contains__(letter):
            prob_dict[letter] += 1
        if russian_uppercase.__contains__(letter):
            prob_dict[letter.lower()] += 1
    for key in prob_dict:
        prob_dict[key] = round(prob_dict[key]/text_length, 4)  
    return prob_dict




prob_letters_dict = teach_function()
#print(prob_letters_dict)

text_path = os.path.join('./texts', 'got1_coded.txt')
file = open(text_path, 'r')
read_text = file.read()
file.close()

text_length = len(read_text)

coded_dict = dict((letter, 0) for letter in russian_lowercase)

for letter in read_text:
    if russian_lowercase.__contains__(letter):
        coded_dict[letter] += 1
    if russian_uppercase.__contains__(letter):
        coded_dict[letter.lower()] += 1

#print(coded_dict);

for key in coded_dict:
    coded_dict[key] = round(coded_dict[key]/text_length, 4)    

sorted_coded_dict = sorted(coded_dict.items(), key=operator.itemgetter(1))
prob_dict = dict((letter, 0) for letter in russian_lowercase)

res_dict = {};

for el in coded_dict:
    min_sub = 1;
    tmp_key = 0;
    for element in prob_letters_dict:
        if abs(coded_dict[el] - prob_letters_dict[element]) < min_sub:
            min_sub = abs(coded_dict[el] - prob_letters_dict[element])
            tmp_key = element
    res_dict[el] = (ord(el) - ord(tmp_key) + alphabet_length) % alphabet_length
    
print(res_dict);
    
sub_dict = {}
for item in res_dict:
    if res_dict[item] in sub_dict:
        sub_dict[res_dict[item]] += 1
    else:
        sub_dict[res_dict[item]] = 1

sorted_sub_dict = sorted(sub_dict.items(), key=operator.itemgetter(1), reverse = True)

key = sorted_sub_dict[0][0]
#print(key)

decoded_text = ''
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

text_decoded_path = os.path.join('./texts', 'decoded_without_key.txt')
res_file = open(text_decoded_path, 'w+')

res_file.write(decoded_text)
res_file.close()
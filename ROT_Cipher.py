#ROT Alphabet Cipher

#User enters word and sets the rotation of the cipher

import string

alpha_string = string.ascii_letters # acquire the larger alphabet as a string

user_word = input('Please enter a word.')
rot_count = int(input('How many characters would you like the encryption/rotation to be?'))
rot_cipher_string = alpha_string[rot_count:] + alpha_string[:rot_count]

code_word = ''
for char in user_word:
    char_index = alpha_string.find(char)      # collect the indeces
    code_word += rot_cipher_string[char_index]  #encrypted based on same indeces but within the rotated alphabet
print(code_word)






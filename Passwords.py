import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = ''

quantity = int(input('Сколько паролей вам нужно? '))
length = int(input('Какой длины должен быть пароль? '))
digit_on = input('Включать в пароль цифры? ')
lowercase_on = input('Включать в пароль прописные буквы (A,B,C,..)? ')
uppercase_on = input('Включать в пароль строчные буквы (a,b,c,..)? ')
punct_on = input('Включать в пароль символы (!#$%&*+-=?@^_.)? ')
amb_on = input('Исключить неоднозначные символы (il1Lo0O)? ')

if digit_on == 'д':
    chars += digits
if lowercase_on == 'д':
    chars += lowercase_letters
if uppercase_on == 'д':
    chars += uppercase_letters
if punct_on == 'д':
    chars += punctuation
if amb_on == 'д':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

def generate_password(length, chars):
    password = '' 
    for _ in range(length):
        password += random.choice(chars)
    return password

for _ in range(quantity):
    print(generate_password(length, chars))  
def encryption(len_alph, case, step, message):
    result = ''
    for i in message:
        if i.isalpha():
            k = ord(i)+step  # шифровка

            if i.isupper():
                case = case.upper()
            elif i.islower():
                case = case.lower()

            if k > ord(case):
                k = k - len_alph

            result += chr(k)

        else:
            result += i

    return result


def decryption(len_alph, case, step, message):
    result = ''
    for i in message:
        if i.isalpha():
            k = ord(i)-step  # шифровка

            if i.isupper():
                case = case.upper()
            elif i.islower():
                case = case.lower()

            if k < ord(case):
                k = k + len_alph

            result += chr(k)

        else:
            result += i

    return result


def main():
    direction = input('Шифрование или дешифрование(e/d)? ')

    language = input('Язык (ru/en): ')
    if language == 'ru':
        len_alph = 32
        alpha = 'а'  # русская
        omega = 'я'
    elif language == 'en':
        len_alph = 26 
        alpha = 'a'  # english
        omega = 'z'  

    step = int(input('Шаг сдвига: '))

    message = input('Введите текст: ')

    if direction == 'e':
        print('Де/Шифровка:', encryption(len_alph, omega, step, message), end='\n')
    elif direction == 'd':
        print('Де/Шифровка:', decryption(len_alph, alpha, step, message), end='\n')

main()
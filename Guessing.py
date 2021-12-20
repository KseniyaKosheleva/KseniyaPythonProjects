import random
x = random.randint(1, 100)

print('Добро пожаловать в числовую угадайку')


def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100


print('Введите целое число от 1 до 100')

flag = True
while flag == True:
    num = input()
    if not is_valid(num):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    else:
        num = int(num)

        if num < x:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif num > x:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            flag = False

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

import random

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом'
            'Мне кажется да', 'Вероятнее всего','Хорошие перспективы', 'Знаки говорят - да', 'Да',
            'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
            'Сконцентрируйся и спроси опять','Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
            'Перспективы не очень хорошие', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как тебя зовут?')
name = input()
print('Привет,', name)

flag = True
while flag == True:
    question = input('Спрашивай, и получишь ответ: ')
    print(random.choice(answers))
    ans_user = input('Хочешь узнать что-то ещё? (д = Да, н = Нет): ')
    if ans_user == 'д':
        continue
    elif ans_user == 'н':
        flag = False
        print('Возвращайся если возникнут вопросы!')

'''ans_user = 'д'
while ans_user = 'д'
    ...
    if not ans_user = 'д':
        print('Возвращайся если возникнут вопросы!')'''
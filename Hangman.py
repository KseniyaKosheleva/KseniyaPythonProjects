import random

word_list = ['погода','время']

def get_word():
    word = random.choice(word_list).upper()
    return word

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word, tries):
    print('Давайте играть в угадайку слов!')
    print(display_hangman(6))
    print('Количество попыток:', tries)
    print('_' * len(word))

    guess = input()
    guess_list = []
    if not guess.isalpha():
        return 'Вы ввели неверный символ, попробуйте снова' 
    elif guess == word:
        return 'Поздравляем, вы угадали слово! Вы победили!'
    elif guess in word:
        guess_list.append(guess)
        return 


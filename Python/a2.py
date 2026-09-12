## Word guessing game

import random

guesses_made = ''


list_words = [
    'game', 'security', 'computer', 'technology', 'phone',
    'book', 'mouse', 'monitor', 'cursor', 'loot',
    'box', 'virtual', 'new', 'theory', 'image'
]

win_word = random.choice(list_words)
ww_lenght = len(win_word)

def rules():
    print('Guess the word by choosing letters')

player = ''
tried = 0
life = round((1.7*len(win_word))+1)

win = False

rules()

while True:
    print(f'You have {life} attempts')
    attempt = input('\nType a letter: ').strip().lower()

    if len(attempt) == 1 and attempt.isalpha() and attempt in win_word:
        print('Nice!')
        player += attempt
        tried += 1
        life -= 1
    elif len(attempt) == 1 and attempt.isalpha() and attempt not in win_word:
        print('Bad..')
        tried += 1
        life -= 1
    elif len(attempt) != 1 or not attempt.isalpha():
        print('Type a valid character from the alphabet!')

    show = ''
    for letter in win_word:
        if letter in player:
            show += letter
            print(letter, end=' ')
        else:
            show += '_'
            print('_', end=' ')

    print('\n')

    if show == win_word:
        win = True
        print(f'Congrats! You got the word!\n' \
        f'In: {tried} attempts with {life} reamaining' )
        break
    elif life <= 0:
        print('Game over! Out of tries ;-;')
        break
    print()
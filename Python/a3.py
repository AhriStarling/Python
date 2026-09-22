import random 

colors = ['purple', 'black', 'gold', 'silver', 'grey']
word = random.choice(colors)

##keeping numbers and counts
tries = 0
hits = 0
hit_letter = []
miss = 0
letter = ''

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

win = False

print('Hangman time! You got 7 tries 0o0')
print("It's a color!")

while True:
    letter = input('\n Type your letter: ') \
    .strip().lower()

##conditions to accept guessed letter
    if len(letter) == 1 and letter.isalpha() and \
    letter in word:
        print ('\nHit!')
        hits += 1
        tries += 1
        hit_letter.append(letter) ## * check this later
    elif len(letter) == 1 and letter.isalpha() \
    and letter not in word:
        print('Miss :(')
        miss += 1
        ## hangman time
        print(hangman[miss])
        tries += 1
    else: ## trying to no specify anything here
        print('ERROR! TRY AGAIN')

    display = ''
    for w in word:
        if w in hit_letter:
            display += w
            print(w, end='')
        else: 
            display += '_'
            print('_', end=' ')

    print('\n')

    if display == word:
        win = True
        print(f'Hooray! lol \n You got it in {tries} tries, ' \
            f'{hits} hits and {miss} miss(es)')
        break

    elif miss >= 5:
        print('Game over, womp :(')
        print(f'The color was {word}')
        break
    

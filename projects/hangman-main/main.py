import os
from random import choice
from hangman_words import word_list

chosen_word = choice(word_list)
answer = ['_' for _ in chosen_word]
found = False
lifes = 6


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


while not found and lifes > 0:
    guess = input("Digite uma letra: ").lower()
    clear()
    mistakes = 0
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            answer[position] = letter
        else:
            mistakes = mistakes + 1
            if mistakes == len(chosen_word):
                lifes = lifes - 1
    print(answer)
    if not '_' in answer:
        found = True
        break
    print(f'Tentativas restantes: {lifes}')

if lifes == 0:
    print(f'Você perdeu. A palavra era "{chosen_word}".')

if found:
    print('Você ganhou!')

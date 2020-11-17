import time
import random
import os


def card_found_check(state, c_c, n_a, last_tried_card, possibility, n_t):
    if state == False:
        print('tried: ', last_tried_card)
        card_guess(c_c, n_a, possibility, n_t)
    else: print('\033[32m' + 'card founded:',last_tried_card, 'number of tries:', n_t, '\033[39m')

def biggest_number_founder(n_a):
    i = 0
    while i < len(n_a):
        compare_number = 0
        temp_array_number = numbers[i]
        if temp_array_number > compare_number:
            compare_number = temp_array_number
        i += 1
    return compare_number

def card_guess(chossen_card, numbers_array, possibility, n_t):
    n_t += 1
    founded = False
    bnf = biggest_number_founder(numbers_array)
    possible = random.randint(1, bnf)
    #
    while numbers.count(possible) == 0:
        possible = random.randint(1, bnf)
    #
    print('precentage of getting right guess: ' + '%',main_possibility/len(numbers))
    if possible == chossen_card:
        founded = True
    numbers.remove(possible)
    card_found_check(founded, chossen_card, numbers_array, possible, possibility, n_t)


os.system('clear')
argu = input('please choose a card between 1-10: ')
card = int(argu)
main_possibility = 100
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tries = 0
card_guess(card, numbers, main_possibility, tries)

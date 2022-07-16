# Kamień, papier, nożyce - 15.07.2022

import random as rnd

RULES = 3

moves = ['K', 'P', 'N']
win_combinations = [('K', 'P'), ('P', 'N'), ('N', 'K')]  # (comp, user)
lose_combinations = [('P', 'K'), ('N', 'P'), ('K', 'N')]  # (comp, user)

def comp_choice():
    comp_move = rnd.choices(moves)
    return comp_move[0]


def user_choice():
    while True:
        choice = input('Podaj K/P/N: ')
        if choice.upper() in moves:
            return choice.upper()
            break
        else:
            print('Podaj poprawną wartość - dozwolone wartości: K/P/N')


def final_raport(counter_user:int, counter_com:int) -> None:

    print('-----------')
    print('Koniec gry!')
    print()

    if counter_user == RULES:
        print(f'Gratulacje! Wygrałeś {counter_user}:{counter_com}')
    else:
        print(f'Przegrałeś! {counter_user}:{counter_com}')


def main():
    counter_com = 0
    counter_user = 0

    while True:
        if counter_com == RULES or counter_user == RULES:
            break
        
        comp_move = comp_choice()
        user_move = user_choice()

        print('Komputer wylosował:', comp_move)
        
        if (comp_move, user_move) in win_combinations:
            counter_user += 1
            print(f'Wygrałeś rundę! {counter_user}:{counter_com}')
        elif (comp_move, user_move) in lose_combinations:
            counter_com += 1
            print(f'Przegrałeś rundę! {counter_user}:{counter_com}')
        else:
            print(f'Remis {counter_user}:{counter_com}')

    final_raport(counter_user, counter_com)


if __name__ == '__main__':
    main()

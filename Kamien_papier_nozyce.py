# Gra "Kamień, papier, nożyce" - do trzech wygranych

import random as rnd

possible_move = ['kamień', 'papier', 'nożyce']

runda1_computer = rnd.choices(possible_move, k=10)
runda1_user = []

runda2_computer = rnd.choices(possible_move, k=10)
runda2_user = []

runda3_computer = rnd.choices(possible_move, k=10)
runda3_user = []

runda4_computer = rnd.choices(possible_move, k=10)
runda4_user = []

runda5_computer = rnd.choices(possible_move, k=10)
runda5_user = []

user_choice = runda1_user.append(input('Podaj kamień, papier czy nożyce: '))

#if user_choice != 'kamień' or user_choice != 'papier' or user_choice != 'nożyce':


print('Komputer wylosował:', runda1_computer[0])

i = 0
while runda1_user[i] == runda1_computer[i]:
    print('Remis - 0:0')
    runda1_user.append(input('Podaj kamień, papier czy nożyce: '))
    i = i+1
    print('Komputer wylosował:', runda1_computer[i])

if (runda1_user[-1] == 'kamień' and runda1_computer[i] == 'papier') or (runda1_user[-1] == 'papier' and runda1_computer[i] == 'nożyce') or (runda1_user[-1] == 'nożyce' and runda1_computer[i] == 'kamień'):
    print('Przegrałeś! - 0:1')
    runda2_user.append(input('Podaj kamień, papier czy nożyce: '))
    print('Komputer wylosował:', runda2_computer[0])

    i = 0
    while runda2_user[i] == runda2_computer[i]:
        print('Remis - nadal 0:1')
        runda2_user.append(input('Podaj kamień, papier czy nożyce: '))
        i = i+1
        print('Komputer wylosował:', runda2_computer[i])

    if (runda2_user[-1] == 'kamień' and runda2_computer[i] == 'papier') or (runda2_user[-1] == 'papier' and runda2_computer[i] == 'nożyce') or (runda2_user[-1] == 'nożyce' and runda2_computer[i] == 'kamień'):
        print('Przegrałeś! - 0:2')
        runda3_user.append(input('Podaj kamień, papier czy nożyce: '))
        print('Komputer wylosował:', runda3_computer[0])

        i = 0
        while runda3_user[i] == runda3_computer[i]:
            print('Remis - nadal 0:2')
            runda3_user.append(input('Podaj kamień, papier czy nożyce: '))
            i = i+1
            print('Komputer wylosował:', runda3_computer[i])

        if (runda3_user[-1] == 'kamień' and runda3_computer[i] == 'papier') or (runda3_user[-1] == 'papier' and runda3_computer[i] == 'nożyce') or (runda3_user[-1] == 'nożyce' and runda3_computer[i] == 'kamień'):
            print('Przegrałeś! - 0:3')
            print('KONIEC GRY')
        else:
            print('Wygrałeś! - 1:2')
            runda4_user.append(input('Podaj kamień, papier czy nożyce: '))
            print('Komputer wylosował:', runda4_computer[0])

            i = 0
            while runda4_user[i] == runda4_computer[i]:
                print('Remis - nadal 1:2')
                runda4_user.append(input('Podaj kamień, papier czy nożyce: '))
                i = i+1
                print('Komputer wylosował:', runda4_computer[i])

            if (runda4_user[-1] == 'kamień' and runda4_computer[i] == 'papier') or (runda4_user[-1] == 'papier' and runda4_computer[i] == 'nożyce') or (runda4_user[-1] == 'nożyce' and runda4_computer[i] == 'kamień'):
                print('Przegrałeś! - 1:3')
                print('KONIEC GRY')
            else:
                print('Wygrałeś! - 2:2')
                runda5_user.append(input('Podaj kamień, papier czy nożyce: '))
                print('Komputer wylosował:', runda5_computer[0])
                
                i = 0
                while runda5_user[i] == runda5_computer[i]:
                    print('Remis - nadal 2:2')
                    runda5_user.append(input('Podaj kamień, papier czy nożyce: '))
                    i = i+1
                    print('Komputer wylosował:', runda5_computer[i])

                if (runda5_user[-1] == 'kamień' and runda5_computer[i] == 'papier') or (runda5_user[-1] == 'papier' and runda5_computer[i] == 'nożyce') or (runda5_user[-1] == 'nożyce' and runda5_computer[i] == 'kamień'):
                    print('Przegrałeś! - 2:3')
                    print('KONIEC GRY')
                else:
                    print('Wygrałeś! - 3:2')
                    print('KONIEC GRY')

    else:
        print('Wygrałeś! - 1:1')
        runda3_user.append(input('Podaj kamień, papier czy nożyce: '))
        print('Komputer wylosował:', runda3_computer[0])

        i = 0
        while runda3_user[i] == runda3_computer[i]:
            print('Remis - nadal 1:1')
            runda3_user.append(input('Podaj kamień, papier czy nożyce: '))
            i = i+1
            print('Komputer wylosował:', runda3_computer[i])

        if (runda3_user[-1] == 'kamień' and runda3_computer[i] == 'papier') or (runda3_user[-1] == 'papier' and runda3_computer[i] == 'nożyce') or (runda3_user[-1] == 'nożyce' and runda3_computer[i] == 'kamień'):
            print('Przegrałeś! - 1:2')
            runda4_user.append(input('Podaj kamień, papier czy nożyce: '))
            print('Komputer wylosował:', runda4_computer[0])

            i = 0
            while runda4_user[i] == runda4_computer[i]:
                print('Remis - nadal 1:2')
                runda4_user.append(input('Podaj kamień, papier czy nożyce: '))
                i = i+1
                print('Komputer wylosował:', runda4_computer[i])

            if (runda4_user[-1] == 'kamień' and runda4_computer[i] == 'papier') or (runda4_user[-1] == 'papier' and runda4_computer[i] == 'nożyce') or (runda4_user[-1] == 'nożyce' and runda4_computer[i] == 'kamień'):
                print('Przegrałeś! - 1:3')
                print('KONIEC GRY')
            else:
                print('Wygrałeś! - 2:2')
                runda5_user.append(input('Podaj kamień, papier czy nożyce: '))
                print('Komputer wylosował:', runda5_computer[0])
                
                i = 0
                while runda5_user[i] == runda5_computer[i]:
                    print('Remis - nadal 2:2')
                    runda5_user.append(input('Podaj kamień, papier czy nożyce: '))
                    i = i+1
                    print('Komputer wylosował:', runda5_computer[i])

                if (runda5_user[-1] == 'kamień' and runda5_computer[i] == 'papier') or (runda5_user[-1] == 'papier' and runda5_computer[i] == 'nożyce') or (runda5_user[-1] == 'nożyce' and runda5_computer[i] == 'kamień'):
                    print('Przegrałeś! - 2:3')
                    print('KONIEC GRY')
                else:
                    print('Wygrałeś! - 3:2')
                    print('KONIEC GRY')
        else:
            print('Wygrałeś! - 2:1')
            runda4_user.append(input('Podaj kamień, papier czy nożyce: '))
            print('Komputer wylosował:', runda4_computer[0])

            i = 0
            while runda4_user[i] == runda4_computer[i]:
                print('Remis - nadal 2:1')
                runda4_user.append(input('Podaj kamień, papier czy nożyce: '))
                i = i+1
                print('Komputer wylosował:', runda4_computer[i])

            if (runda4_user[-1] == 'kamień' and runda4_computer[i] == 'papier') or (runda4_user[-1] == 'papier' and runda4_computer[i] == 'nożyce') or (runda4_user[-1] == 'nożyce' and runda4_computer[i] == 'kamień'):
                print('Przegrałeś! - 2:2')
                runda5_user.append(input('Podaj kamień, papier czy nożyce: '))
                print('Komputer wylosował:', runda5_computer[0])
                
                i = 0
                while runda5_user[i] == runda5_computer[i]:
                    print('Remis - nadal 2:2')
                    runda5_user.append(input('Podaj kamień, papier czy nożyce: '))
                    i = i+1
                    print('Komputer wylosował:', runda5_computer[i])

                if (runda5_user[-1] == 'kamień' and runda5_computer[i] == 'papier') or (runda5_user[-1] == 'papier' and runda5_computer[i] == 'nożyce') or (runda5_user[-1] == 'nożyce' and runda5_computer[i] == 'kamień'):
                    print('Przegrałeś! - 2:3')
                    print('KONIEC GRY')
                else:
                    print('Wygrałeś! - 3:2')
                    print('KONIEC GRY')
            else:
                print('Wygrałeś! - 3:1')
                print('KONIEC GRY')
else:
    print('Wygrałeś! - 1:0')
    runda2_user.append(input('Podaj kamień, papier czy nożyce: '))
    print('Komputer wylosował:', runda2_computer[0])

    i = 0
    while runda2_user[i] == runda2_computer[i]:
        print('Remis - nadal 1:0')
        runda2_user.append(input('Podaj kamień, papier czy nożyce: '))
        i = i+1
        print('Komputer wylosował:', runda2_computer[i])

    if (runda2_user[-1] == 'kamień' and runda2_computer[i] == 'papier') or (runda2_user[-1] == 'papier' and runda2_computer[i] == 'nożyce') or (runda2_user[-1] == 'nożyce' and runda2_computer[i] == 'kamień'):
        print('Przegrałeś! - 1:1')
        runda3_user.append(input('Podaj kamień, papier czy nożyce: '))
        print('Komputer wylosował:', runda3_computer[0])

        i = 0
        while runda3_user[i] == runda3_computer[i]:
            print('Remis - nadal 1:1')
            runda3_user.append(input('Podaj kamień, papier czy nożyce: '))
            i = i+1
            print('Komputer wylosował:', runda3_computer[i])

        if (runda3_user[-1] == 'kamień' and runda3_computer[i] == 'papier') or (runda3_user[-1] == 'papier' and runda3_computer[i] == 'nożyce') or (runda3_user[-1] == 'nożyce' and runda3_computer[i] == 'kamień'):
            print('Przegrałeś! - 1:2')
            runda4_user.append(input('Podaj kamień, papier czy nożyce: '))
            print('Komputer wylosował:', runda4_computer[0])

            i = 0
            while runda4_user[i] == runda4_computer[i]:
                print('Remis - nadal 1:2')
                runda4_user.append(input('Podaj kamień, papier czy nożyce: '))
                i = i+1
                print('Komputer wylosował:', runda4_computer[i])

            if (runda4_user[-1] == 'kamień' and runda4_computer[i] == 'papier') or (runda4_user[-1] == 'papier' and runda4_computer[i] == 'nożyce') or (runda4_user[-1] == 'nożyce' and runda4_computer[i] == 'kamień'):
                print('Przegrałeś! - 1:3')
                print('KONIEC GRY')
            else:
                print('Wygrałeś! - 2:2')
                runda5_user.append(input('Podaj kamień, papier czy nożyce: '))
                print('Komputer wylosował:', runda5_computer[0])
                
                i = 0
                while runda5_user[i] == runda5_computer[i]:
                    print('Remis - nadal 2:2')
                    runda5_user.append(input('Podaj kamień, papier czy nożyce: '))
                    i = i+1
                    print('Komputer wylosował:', runda5_computer[i])

                if (runda5_user[-1] == 'kamień' and runda5_computer[i] == 'papier') or (runda5_user[-1] == 'papier' and runda5_computer[i] == 'nożyce') or (runda5_user[-1] == 'nożyce' and runda5_computer[i] == 'kamień'):
                    print('Przegrałeś! - 2:3')
                    print('KONIEC GRY')
                else:
                    print('Wygrałeś! - 3:2')
                    print('KONIEC GRY')
        else:
            print('Wygrałeś! - 2:1')
            runda4_user.append(input('Podaj kamień, papier czy nożyce: '))
            print('Komputer wylosował:', runda4_computer[0])

            i = 0
            while runda4_user[i] == runda4_computer[i]:
                print('Remis - nadal 2:1')
                runda4_user.append(input('Podaj kamień, papier czy nożyce: '))
                i = i+1
                print('Komputer wylosował:', runda4_computer[i])

            if (runda4_user[-1] == 'kamień' and runda4_computer[i] == 'papier') or (runda4_user[-1] == 'papier' and runda4_computer[i] == 'nożyce') or (runda4_user[-1] == 'nożyce' and runda4_computer[i] == 'kamień'):
                print('Przegrałeś! - 2:2')
                runda5_user.append(input('Podaj kamień, papier czy nożyce: '))
                print('Komputer wylosował:', runda5_computer[0])
                
                i = 0
                while runda5_user[i] == runda5_computer[i]:
                    print('Remis - nadal 2:2')
                    runda5_user.append(input('Podaj kamień, papier czy nożyce: '))
                    i = i+1
                    print('Komputer wylosował:', runda5_computer[i])

                if (runda5_user[-1] == 'kamień' and runda5_computer[i] == 'papier') or (runda5_user[-1] == 'papier' and runda5_computer[i] == 'nożyce') or (runda5_user[-1] == 'nożyce' and runda5_computer[i] == 'kamień'):
                    print('Przegrałeś! - 2:3')
                    print('KONIEC GRY')
                else:
                    print('Wygrałeś! - 3:2')
                    print('KONIEC GRY')
            else:
                print('Wygrałeś! - 3:1')
                print('KONIEC GRY')
    else:
        print('Wygrałeś! - 2:0')
        runda3_user.append(input('Podaj kamień, papier czy nożyce: '))
        print('Komputer wylosował:', runda3_computer[0])

        i = 0
        while runda3_user[i] == runda3_computer[i]:
            print('Remis - nadal 2:0')
            runda3_user.append(input('Podaj kamień, papier czy nożyce: '))
            i = i+1
            print('Komputer wylosował:', runda3_computer[i])

        if (runda3_user[-1] == 'kamień' and runda3_computer[i] == 'papier') or (runda3_user[-1] == 'papier' and runda3_computer[i] == 'nożyce') or (runda3_user[-1] == 'nożyce' and runda3_computer[i] == 'kamień'):
            print('Przegrałeś! - 2:1')
            runda4_user.append(input('Podaj kamień, papier czy nożyce: '))
            print('Komputer wylosował:', runda4_computer[0])

            i = 0
            while runda4_user[i] == runda4_computer[i]:
                print('Remis - nadal 2:1')
                runda4_user.append(input('Podaj kamień, papier czy nożyce: '))
                i = i+1
                print('Komputer wylosował:', runda4_computer[i])

            if (runda4_user[-1] == 'kamień' and runda4_computer[i] == 'papier') or (runda4_user[-1] == 'papier' and runda4_computer[i] == 'nożyce') or (runda4_user[-1] == 'nożyce' and runda4_computer[i] == 'kamień'):
                print('Przegrałeś! - 2:2')
                runda5_user.append(input('Podaj kamień, papier czy nożyce: '))
                print('Komputer wylosował:', runda5_computer[0])
                
                i = 0
                while runda5_user[i] == runda5_computer[i]:
                    print('Remis - nadal 2:2')
                    runda5_user.append(input('Podaj kamień, papier czy nożyce: '))
                    i = i+1
                    print('Komputer wylosował:', runda5_computer[i])

                if (runda5_user[-1] == 'kamień' and runda5_computer[i] == 'papier') or (runda5_user[-1] == 'papier' and runda5_computer[i] == 'nożyce') or (runda5_user[-1] == 'nożyce' and runda5_computer[i] == 'kamień'):
                    print('Przegrałeś! - 2:3')
                    print('KONIEC GRY')
                else:
                    print('Wygrałeś! - 3:2')
                    print('KONIEC GRY')
            else:
                print('Wygrałeś! - 3:1')
                print('KONIEC GRY')
        else:
            print('Wygrałeś! - 3:0')
            print('KONIEC GRY')
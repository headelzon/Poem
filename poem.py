# WFK 2014
# Project: Poem generator
# Basics of informatics
import rhymes
from pathlib import Path


def is_valid(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print('Use a number. Try again!')
            continue

        if value < low or value > high:
            print('Use a number between 1 and 5. Try again!')
            continue
        else:
            break
    return value


def menu():
    print('\nWhat type of rhymes shall the poem have?')
    print('1) AABB')
    print(' 2) ABBA')
    print('  3) ABAB')
    print('   4) Other')
    print('    5) Exit \n')


def save(poem):
    print('\nDo you wish to save the poem to external .txt file?')
    choice = input('Y/N  ')
    number = 0

    if choice == 'Y' or choice == 'y':
        while True:
            number = str(number)
            if number == '0':
                number = ''
            name = 'poem' + number + '.txt'
            f = Path(name)
            if f.is_file():  # if file exists
                if name == 'poem.txt':
                    number = 0
                number = int(number)
                number += 1
            else:
                break

        f = open(name, 'w+')

        for x in poem:
            f.write(x + '\n')

        print('Poem saved as {} in main directory.'.format(name))
        f.close()

    elif choice == 'N' or choice == 'n':
        pass


def main():
    print('\n\t--- POEM GENERATOR ---\n\n')

    while True:
        menu()
        choice = is_valid('Your choice: ', 1, 5)

        if choice == 1:
            verses = is_valid('Please input number of stanzas (verses) 1-9: ', 1, 9)
            print('')
            aabb = rhymes.aabb(verses)
            save(aabb)
        elif choice == 2:
            verses = is_valid('Please input number of stanzas (verses) 1-9: ', 1, 9)
            print('')
            abba = rhymes.abba(verses)
            save(abba)
        elif choice == 3:
            verses = is_valid('Please input number of stanzas (verses) 1-9: ', 1, 9)
            print('')
            abab = rhymes.abab(verses)
            save(abab)
        elif choice == 4:
            print('\tChoose from below:')
            print('\t1) A blank verse (no rhymes)')
            print('\t 2) A sonnet (2 stanzas with 4 lines and 2 stanzas with 3 lines')
            print('\t  3) Back\n')
            choice2 = is_valid('Your choice: ', 1, 3)

            while True:
                if choice2 == 1:
                    verses = is_valid('Please input number of stanzas (verses) 1-20: ', 1, 20)
                    print('')
                    blank = rhymes.blank(verses)
                    save(blank)
                    break
                elif choice2 == 2:
                    sonnet = rhymes.sonnet()
                    save(sonnet)
                    break
                else:
                    break

        elif choice == 5:
            print('Bye!')
            break

if __name__ == "__main__":
    main()

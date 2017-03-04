# WFK 2014
# Project: Poem generator
# Basics of informatics
import rhymes


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


# def save():
# instead of printing lines in rhymes.py append them to list poem[] and then print
# to save, just write in consecutive entities of the list poem[]

def main():
    loop = True
    print('\n\t--- POEM GENERATOR ---\n\n')

    while loop:
        menu()
        choice = is_valid('Your choice: ', 1, 5)

        if choice == 1:
            verses = is_valid('Please input number of stanzas (verses) 1-9: ', 1, 9)
            print('')
            rhymes.aabb(verses)
        elif choice == 2:
            verses = is_valid('Please input number of stanzas (verses) 1-9: ', 1, 9)
            print('')
            rhymes.abba(verses)
        elif choice == 3:
            verses = is_valid('Please input number of stanzas (verses) 1-9: ', 1, 9)
            print('')
            rhymes.abab(verses)
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
                    rhymes.blank(verses)
                    break
                elif choice2 == 2:
                    print('Sonnet under construction!')
                    break
                else:
                    break

        elif choice == 5:
            print('Bye!')
            loop = False

if __name__ == "__main__":
    main()

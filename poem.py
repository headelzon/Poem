# WFK 2014
# Project: Poem generator
# Basics of informatics
import rhymes


def is_valid(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print('Use a number. Try again!')
            continue

        if value < 1 or value > 5:
            print('Use a number between 1 and 5. Try again!')
            continue
        else:
            break
    return value


def menu():
    print('\n\t--- POEM GENERATOR ---\n\n')
    print('What type of rhymes shall the poem have?')
    print('1) AABB')
    print(' 2) ABBA')
    print('  3) ABAB')
    print('   4) Other')
    print('    5) Exit \n')


def main():
    loop = True

    while loop:
        menu()
        choice = is_valid('Your choice: ')

        if choice == 1:
            print('AABB')
            # AABB
        elif choice == 2:
            print('ABBA')
            # ABBA
        elif choice == 3:
            print('ABAB')
            verses = int(input('Please input number of stanzas (verses) 1-9: '))
            print('')
            rhymes.abab(verses)
        elif choice == 4:
            print('Other')
            # Other
        elif choice == 5:
            print('Bye!')
            loop = False

if __name__ == "__main__":
    main()

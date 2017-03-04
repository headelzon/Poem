# Rhymes module
import random


def abab(verse):
    f = open('a.txt', 'r')
    g = open('b.txt', 'r')

    a, b, numbers = [], [], []

    for line in f:
        line2 = line.replace("\n", "")  # Delete newline at the end of each line
        a.append(line2)

    for line in g:
        line2 = line.replace("\n", "")
        b.append(line2)

    how_long = min(len(a), len(b))  # range of random numbers based on smallest rhyme database

    for x in range(verse):
        while True:
            line = random.randrange(how_long)
            if line in numbers:
                continue
            else:
                numbers.append(line)
                break

    for x in range(verse):
        if x % 2 == 0:
            print(a[numbers[x]])
        else:
            print(b[numbers[x]])


def aabb(verse):
    f = open('a.txt', 'r')
    g = open('b.txt', 'r')

    a, b, numbers = [], [], []

    for line in f:
        line2 = line.replace("\n", "")  # Delete newline at the end of each line
        a.append(line2)

    for line in g:
        line2 = line.replace("\n", "")
        b.append(line2)

    how_long = min(len(a), len(b))

    for x in range(verse):
        while True:
            line = random.randrange(how_long) # random numbers generation
            if line in numbers:
                continue
            else:
                numbers.append(line)
                break

    # AABB
    # For x divisible by 4 (0, 4, 8, 12, ...) + 1 (1, 5, 9, 13, ...) - rhyme A
    # For x divisible by 2 but not by 4 and not 0 (2, 6, 10, 14, ...) + 1 (3, 7, 11, 15, ...) - rhyme B

    for x in range(verse):
        if x % 4 == 0:
            print(a[numbers[x]]) # print random (from list numbers[]) element of list a or b
        elif (x-1) % 4 == 0:
            print(a[numbers[x]])
        elif (x % 2 == 0) and (x % 4 != 0):
            print(b[numbers[x]])
        else:
            print(b[numbers[x]])


# ABBA
# For x divisible by 3 (0, 3, 6, 9, ...) - rhyma A
# For other - rhyme B

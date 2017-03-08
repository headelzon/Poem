# Rhymes module
import random


def abab(verse):
    f = open('a.txt', 'r')
    g = open('b.txt', 'r')

    a, b, numbers, poem = [], [], [], []

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
            poem.append(a[numbers[x]])
        else:
            poem.append(b[numbers[x]])

    for x in poem:
        print(x)

    return poem


def aabb(verse):
    f = open('a.txt', 'r')
    g = open('b.txt', 'r')

    a, b, numbers, poem = [], [], [], []

    for line in f:
        line2 = line.replace("\n", "")  # Delete newline at the end of each line
        a.append(line2)

    for line in g:
        line2 = line.replace("\n", "")
        b.append(line2)

    how_long = min(len(a), len(b))

    for x in range(verse):
        while True:
            line = random.randrange(how_long)  # random numbers generation
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
            poem.append(a[numbers[x]])  # print random (from list numbers[]) element of list a or b
        elif (x - 1) % 4 == 0:
            poem.append(a[numbers[x]])
        elif (x % 2 == 0) and (x % 4 != 0):
            poem.append(b[numbers[x]])
        else:
            poem.append(b[numbers[x]])

    for x in poem:
        print(x)

    return poem


def abba(verse):
    f = open('a.txt', 'r')
    g = open('b.txt', 'r')

    a, b, numbers, poem = [], [], [], []

    for line in f:
        line2 = line.replace("\n", "")  # Delete newline at the end of each line
        a.append(line2)

    for line in g:
        line2 = line.replace("\n", "")
        b.append(line2)

    how_long = min(len(a), len(b))

    for x in range(verse):
        while True:
            line = random.randrange(how_long)  # random numbers generation
            if line in numbers:
                continue
            else:
                numbers.append(line)
                break

    # ABBA
    # For x divisible by 3 (0, 3, 6, 9, ...) - rhyma A
    # For other - rhyme B

    for x in range(verse):
        if x % 3 == 0:
            poem.append(a[numbers[x]])
        else:
            poem.append(b[numbers[x]])

    for x in poem:
        print(x)

    return poem


def sonnet():
    f = open('a.txt', 'r')
    g = open('b.txt', 'r')
    h = open('c.txt', 'r')
    i = open('d.txt', 'r')

    a, b, c, d, numbers_a, numbers_b, poem = [], [], [], [], [], [], []

    for line in f:
        line2 = line.replace("\n", "")  # Delete newline at the end of each line
        a.append(line2)  # Append to list a[]

    for line in g:
        line2 = line.replace("\n", "")
        b.append(line2)

    for line in h:
        line2 = line.replace("\n", "")
        c.append(line2)

    for line in i:
        line2 = line.replace("\n", "")
        d.append(line2)

    how_long_a = min(len(a), len(b))
    how_long_b = min(len(c), len(d))

    for x in range(9):
        while True:
            line_a = random.randrange(how_long_a)  # random numbers generation
            if line_a in numbers_a:
                continue
            else:
                numbers_a.append(line_a)
                break

    for x in range(7):
        while True:
            line_b = random.randrange(how_long_b)
            if line_b in numbers_b:
                continue
            else:
                numbers_b.append(line_b)
                break

    for x in range(9):
        if x in [0, 3, 5, 8]:
            poem.append(a[numbers_a[x]])
        elif x in [1, 2, 6, 7]:
            poem.append(b[numbers_a[x]])
        else:
            poem.append('')

    print('')

    for x in range(7):
        if x in [0, 2, 5]:
            poem.append(c[numbers_b[x]])
        elif x == 3:
            poem.append('')
        else:
            poem.append(d[numbers_b[x]])

    for x in poem:
        print(x)

    return poem


def blank(verse):
    f = open('blank.txt', 'r')

    a, numbers, poem = [], [], []

    for line in f:
        line2 = line.replace("\n", "")  # Delete newline at the end of each line
        a.append(line2)  # Append to list a[]

    for x in range(verse):
        while True:
            line = random.randrange(len(a))  # random numbers generation
            if line in numbers:
                continue
            else:
                numbers.append(line)
                break

    for x in range(verse):
        poem.append(a[numbers[x]])

    for x in poem:
        print(x)

    return poem

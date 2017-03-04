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
            print(a[numbers[x]])  # print random (from list numbers[]) element of list a or b
        elif (x - 1) % 4 == 0:
            print(a[numbers[x]])
        elif (x % 2 == 0) and (x % 4 != 0):
            print(b[numbers[x]])
        else:
            print(b[numbers[x]])


def abba(verse):
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
            print(a[numbers[x]])
        else:
            print(b[numbers[x]])


# def sonnet():
#     f = open('a.txt', 'r')
#     g = open('b.txt', 'r')
#     h = open('c.txt', 'r')
#     i = open('d.txt', 'r')
#
#     a, b, c, d, numbers_a, numbers_b = [], [], [], [], [], []
#
#     for line in f:
#         line2 = line.replace("\n", "")  # Delete newline at the end of each line
#         a.append(line2)  # Append to list a[]
#
#     for line in g:
#         line2 = line.replace("\n", "")
#         b.append(line2)
#
#     for line in h:
#         line2 = line.replace("\n", "")
#         c.append(line2)
#
#     for line in i:
#         line2 = line.replace("\n", "")
#         d.append(line2)
#
#     how_long_a = min(len(a), len(b))
#     how_long_b = min(len(c), len(d))
#
#     for x in range(14):
#         while True:
#             line_a = random.randrange(how_long_a)  # random numbers generation
#             line_b = random.randrange(how_long_b)
#             if line_a in numbers_a:
#                 continue
#             elif line_b in numbers_b:
#                 continue
#             else:
#                 numbers_a.append(line_a)
#                 numbers_b.append(line_b)
#
#     for x in range(14):
#         if x in [0, 3, 4, 7]:
#             print(a[numbers_a[x]])
#         elif x in [1, 2, 5, 6]:
#             print(b[numbers_a[x]])
#         elif x in [8, 10, 12]:
#             print(c[numbers_b[x]])
#         else:
#             print(d[numbers_b[x]])


def blank(verse):
    f = open('blank.txt', 'r')

    a, numbers = [], []

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
        print(a[numbers[x]])

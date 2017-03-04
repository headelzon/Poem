# Rhymes module
import random

def abab(verse):
    f = open('a.txt', 'r')
    g = open('b.txt', 'r')

    a, b, numbers = [], [], []

    for line in f:
        line2 = line.replace("\n", "")
        a.append(line2)


    for line in g:
        line2 = line.replace("\n", "")
        b.append(line2)


    how_long = min(len(a), len(b))

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
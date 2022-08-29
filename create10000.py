import random

def add_10000_numbers(filename):
    numbers = []
    for i in range(1000000):
        numbers.append(i)
    random.shuffle(numbers)
    f = open(filename, 'a')
    for i in numbers:
        f.write(f"{i}\n")
    return numbers

add_10000_numbers('./numbers/1000000.txt')
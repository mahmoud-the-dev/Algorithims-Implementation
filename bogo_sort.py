import random

def load_numbers(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line))
    return numbers

def is_sorted(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True


def bogo_sort(list):
    attempts = 0
    while not is_sorted(list):
        attempts += 1
        random.shuffle(list)
    return list, attempts 


numbers = load_numbers('./numbers/8.txt')

sorted = bogo_sort(numbers)

print(sorted)
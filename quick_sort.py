def load_names(filename):
    names = []
    with open(filename) as f:
        for line in f:
            names.append(line.rstrip())
    return names





def load_numbers(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line))
    return numbers

def quick_sort(list):
    if len(list) <= 1:
        return list
    
    less_than_pivot = []
    greater_than_pivot = []

    pivot = list[0]

    for i in list[1:]:
        if i >pivot:
            greater_than_pivot.append(i)
        else:
            less_than_pivot.append(i)
    
    return quick_sort(less_than_pivot) +[pivot]+ quick_sort(greater_than_pivot)


def is_sorted(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True


unsorted_names = load_names("./names/unsorted.txt")

numbers = load_numbers('./numbers/1000000.txt')

sorted_names = quick_sort(unsorted_names)

for name in sorted_names:
    print (name)
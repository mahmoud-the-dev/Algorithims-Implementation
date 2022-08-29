
def load_numbers(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line))
    return numbers

def selection_sort(list):
    sorted_list=[]
    # print("%-25s %-25s" % (list,sorted_list))
    while len(list) > 0:
        index_to_add = index_of_min(list)
        sorted_list.append(list.pop(index_to_add))
        # print("%-25s %-25s" % (list,sorted_list))
    return sorted_list

def index_of_min(list):
    min_index = 0
    for i in range(1,len(list)):
        if list[i] < list[min_index]:
            min_index = i
    return min_index





numbers = load_numbers('./numbers/1000000.txt')

sorted_list =selection_sort(numbers)

print(sorted_list)
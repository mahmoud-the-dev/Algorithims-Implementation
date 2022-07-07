def liner_search (list , target):

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    
    return None

def validate (result):
    if result is None:
        print ("the value doesn't exist")
    else:
        print (f"the value's index is {result}")

numbers = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]
result =liner_search(numbers, 17)

validate(result)
result =liner_search(numbers, 7)
validate(result)
def binary_search(list, target):

    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint=(first+last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint]>target:
            last = midpoint-1
        else:
            first = midpoint+1
    
    return None



def validate (result):
    if result is None:
        print ("the value doesn't exist")
    else:
        print (f"the value's index is {result}")

numbers = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]
result =binary_search(numbers, 17)

validate(result)
result =binary_search(numbers, 7)
validate(result)







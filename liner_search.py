def liner_search (list , target):
    
    for i in range(0, len(list)):
        #return the index position of the target if found
        if list[i] == target:
            return i
    # but if we couldn't find it, we'll just return None
    return None

# a function that checks if the target is found
def validate (result):
    #if the value is not found then result will be None
    if result is None:
        print ("the value doesn't exist")
    #else we just return it's index
    else:
        print (f"the value's index is {result}")

# a list of numbers to test our liner_search function
numbers = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]

# doing the test for number 17
result =liner_search(numbers, 17)

# checking if 17 exist in the list
validate(result)

# doing the test for number 7
result =liner_search(numbers, 7)

# checking if 7 exist in the list
validate(result)

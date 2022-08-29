def binary_search(list, target):
    # we create to variables point to the beginning and the end of the list
    first = 0
    last = len(list) - 1
    # we will be using them to break the list down into sublists while searching

    # we create while loop to keep breaking the list down till we find our the target and return it's index
    while first <= last:
        # we choose the index of the value in the middle of the list 
        midpoint=(first+last)//2

        # we check if the value in the middle of the list/sublist is our target
        if list[midpoint] == target:
            # if it is our target, we return its index
            return midpoint

        #we check if the value in the middle of the list/sublist is more than our target
        elif list[midpoint]>target:
            # if it is more than our target, we break the list down into the first half of the list not including the midpoint 
            # By making our last variable = the midpoint - 1
            last = midpoint-1

        #if the value in the middle of the list/sublist is not more or equal to our target, then it's less than the target
        else:
            # Then we break the list down into the second half of the list not including the midpoint 
            # By making our first variable = the midpoint + 1
            first = midpoint+1
    # if we couldn't find the target we just return None
    return None


# a function that checks if the target is found
def validate (result):
    #if the value is not found then result will be None
    if result is None:
        print ("the value doesn't exist")
    #else we just return it's index
    else:
        print (f"the value's index is {result}")

# numbers = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]
# result =binary_search(numbers, 17)

# validate(result)
# result =binary_search(numbers, 7)
# validate(result)







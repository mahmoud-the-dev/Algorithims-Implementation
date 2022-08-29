# we will do the binary search suing recursion this time
def recursive_binary_search(list,target):
    # the first thing we do is to put our stop condition to stop the recursion
    # when the list is empty that means target is not in the list. 
    # so we use that as our stop condition
    if len(list) == 0:
        return False
    else :
        # we choose the index of the value in the middle of the list 
        midpoint = len(list)//2

        # we check if the value in the middle of the list/sublist is our target
        if list[midpoint] == target:
            # if it is our target, we return True which means we found it
            return True
        
        # if it is not our target, then there are two possible cases
        else:
            #is the value in the middle of the list is larger than the target?
            if list[midpoint] > target:
                #if yes, then we search our target in the first half of the list
                # By calling the function again giving it the first half of the list and the target as arguments
                return recursive_binary_search(list[:midpoint],target)

            #if the value in the middle of the list/sublist is not more or equal to our target, then it's less than the target
            else: 
                #So we search the target in the second half of the list
                # By calling the function again giving it the second half of the list and the target as arguments
                return recursive_binary_search(list[midpoint+1:],target)
        #we keep doing this till find our target and return True or get an empty list and return False

# a function that checks if the target is found
def validate (result):
    print ("Target found: ", result)


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

result = recursive_binary_search(numbers,17)
validate(result)

result = recursive_binary_search(numbers,1)
validate(result)


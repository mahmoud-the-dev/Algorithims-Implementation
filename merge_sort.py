def merge_sort ( list):
    """
    sort list in ascending order
    return a new sorted list

    Divide: Find the midpoint of the list and divide into sublists 
    Conquer: recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes overall O(n log n) time
    """

    if len(list) <= 1:
        return list
    left_part, right_part = split(list)
    left = merge_sort(left_part)
    right = merge_sort(right_part)

    return merge (left, right)


def split ( list ):
    
    """
    Divide the unsorted list at the midpoint into sublists
    Returns two sublists - left_part and right_part

    Takes overall O(log n) time
    """

    mid = len(list)//2

    left = list[:mid]
    right = list[mid:]

    return left, right
    
def merge ( left , right):

    """
    Merges two lists, sorting them in the process
    Returns a new merged list

    Runs in overall O(n) time
    """

    l=[]
    i=0 
    j=0

    while i < len(left) and j <len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else: 
            l.append(right[j])
            j+=1

    while i < len(left) :
        l.append(left[i])
        i+=1

    while j < len(right) :
        l.append(right[j])
        j+=1
    
    return l

def validate (list ):
    if len(list) <=1:
        return True
    return list[0]<=list[1] and validate(list[1:])


numbers = [7,5,3,4,2,100,546,6512,321,321,21,21,21]
print (validate(numbers))
result = merge_sort(numbers)
print (validate(result))

print(result)




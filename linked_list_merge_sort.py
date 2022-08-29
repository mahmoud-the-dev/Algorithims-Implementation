from linked_list import LinkedList

def merge_sort (list):
    """
    Sort a linked list in ascending order

    - Recursively divide linked list into sublists containing a single node 
    - Repeatedly merge the sublists to produce sorted sublists until one remains
    
    - Return a sorted linked list
    """

    if list.size() == 1 or list.Head is None:
        return list
    
    left_half, right_half=split (list)
    left = merge_sort (left_half)
    right = merge_sort (right_half)


    list.Head = merge (left, right).Head
    return list
def split (list):
    """
    Divide a linked list into sublists at the midpoint
    """

    if list is None or list.Head is None:
        left_half = list
        right_half = None
        return left_half, right_half
    else:
        mid= list.size()//2
        
        mid_node= list.node_at(mid-1)
        
        left_half = list
        right_half = LinkedList()
        
        right_half.Head = mid_node.next_node
        mid_node.next_node = None
        
        return left_half, right_half

def merge (left, right):
    """
    Merge two sublists, sorted by data in nodes
    Returns a new, merged list 
    """

    # create a new linked list to contain the merged nodes
    # from left and right
    merged =LinkedList()

    # add a fake Head, will be removed later
    merged.add(0)

    #set current to the head of the list

    current = merged.Head

    #obtain head nodes for left and right linked lists
    left_head = left.Head
    right_head = right.Head


    # iterate over left and right until
    # we reach the tail node of either
    while left_head or right_head :
        # if the head of left is none that means we reached the tail of left 
        # we start adding the nodes from right to the merged linked list
        if left_head is None:
            current.next_node = right_head
            #call next on right to move through right list
            right_head = right_head.next_node
        # if the head of right is none that means we reached the tail of right 
        # we start adding the nodes from left to the merged linked list 
        elif right_head is None:
            current.next_node = left_head
            #call next on left to move through left list
            left_head = left_head.next_node
        else : 
            # if the data in left_head is less than the data in right_head
            # we add the node left head to the merged linked list
            if left_head.data < right_head.data:
                current.next_node = left_head
                #move left head to the next node
                left_head = left_head.next_node

            # if the data in left_head is greater than the data in right_head
            # we add the node right head to the merged linked list
            else:   
                current.next_node = right_head
                #move right head to the next node
                right_head = right_head.next_node
        # move current to next node
        current = current.next_node
    #discard fake head and set first merged node as head
    merged.Head = merged.Head.next_node

    return merged

def validate_order(list):
    if list.Head is None or list.Head.next_node is None:
        return True
    return validate_nodes(list.Head)

def validate_nodes(node):
    if node is None or node.next_node is None:
        return True
    return node.data <= node.next_node.data and validate_nodes(node.next_node)
        

l = LinkedList()

l.add(1)
l.add(130)
l.add(1211)
l.add(102)
l.add(15)
l.add(140)
l.add(153)
l.add(3)
l.add(300)
l.add(1320)
l.add(3)

print(l)
order =validate_order(l)
print(f"order is: {order}")

merge_sort(l)

order =validate_order(l)

print(l)
print(f"order is: {order}")
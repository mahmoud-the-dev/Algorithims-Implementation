class Node:
    data = None
    next_node = None
    
    def __init__(self,data):
        self.data=data

    def __repr__(self):
        return f"<Node : {self.data} >"

class LinkedList:

    def __init__(self):
        self.Head = None
    
    def is_empty(self):
        return self.Head == None
    
    def size(self):
        """
        Returns the number of nodes in the list
        takes O(n) time
        """
        current = self.Head
        count =0
        while current:
            count += 1
            current = current.next_node
        return count
    
    def add (self,data):
        
        """
        Add a new node to the list
        takes O(1) time 
        """

        new_node = Node(data)
        new_node.next_node = self.Head
        self.Head = new_node

    def node_at (self,index):
        """
        Returns the node at specific index
        takes O(n) time
        """
        
        current = self.Head
        position = index

        while position > 0 :
            current = current.next_node
            position -= 1
        
        return current

    def search (self, key):

        """
        Search for first node containing data that matches the key 
        Return the node or 'None' if no such node.

        takes O(n) time
        """

        current= self.Head
        while current:
            if current.data == key:
                return current
            else: 
                current = current.next_node
        return None

    def insert (self,data,index):

        """
        Insert a new node containing data at index position
        insertion takes O(1) time but finding the node 
        at the insertion point takes O(n) time

        Takes overall O(n) time
        """

        if index == 0:
            self.add(data)
        elif index>0:
            new_node = Node(data)
            position = index
            current= self.Head
            while position > 1:
                current=current.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self,key):

        """
        Removes the first node with the given key
        
        it takes O(n) time to find the node with key
        and takes O(1) to delete the node
        Takes overall O(n) time


        Returns the removed node
        """

        current=self.Head
        prev_node=None
        found= False
        while current and not found:
            if current.data == key and current is self.Head:
                self.Head= current.next_node
                found=True
            elif current.data == key:
                prev_node.next_node= current.next_node
                found=True
            else:
                prev_node = current
                current = current.next_node
        return current

    def remove_at(self,index):
        
        """
        Removes the node at specific index
        
        takes O(n) time to find the node 
        and O(1) to delete it
        Takes overall O(n) time

        Returns the removed node
        """
        
        current=self.Head
        prev_node=None
        position = index
        found=False
        while current and not found:
            if position == 0 and current is self.Head:
                self.Head=current.next_node
                found=True
            if position == 0:
                prev_node.next_node = current.next_node
                found=True
            else:
                prev_node = current
                current=current.next_node
                position -=1
        return current

    
    def __repr__(self):

        """
        Return a string representation of the list
        takes O(n) time
        """

        nodes = []
        current= self.Head
        while current:
            if current == self.Head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node:
                nodes.append(f"[{current.data}]")
            else:
                nodes.append(f"[Tail: {current.data}]")
            current=current.next_node
        
        return " -> ".join(nodes)


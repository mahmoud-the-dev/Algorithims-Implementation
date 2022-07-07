position = index
        current= self.Head
        while position > 1:
            current=current.next_node
            position -= 1
        
        prev_node = current
        next_node = current.next_node

        prev_node.next_node = new_node
        
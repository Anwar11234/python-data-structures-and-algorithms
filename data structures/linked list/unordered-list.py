from node import Node

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self , item):
        newItem = Node(item)
        newItem.setnext(self.head)
        self.head = newItem

    def length(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()

        return count  

    def search(self , item):
        current = self.head

        while current != None:
            if current.getData() == item:
                return True
            else:
                current = current.getNext()

        return False                              

    def remove(self , item):
        # assumes the item is in the list

        current = self.head
        prev = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                prev = current
                current = current.getNext()

        
        if prev == None: # the item we want to remove is at the head of the list
            self.head = current.getNext()
        else:
            prev.setnext(current.getNext())              
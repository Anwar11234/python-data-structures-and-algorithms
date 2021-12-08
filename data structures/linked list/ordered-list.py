from node import Node

class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None    

    def length(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()

        return count 

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

    def search(self , item):
        current = self.head

        while current != None:
            if current.getData() == item:
                return True
            else:
                if current.getData() > item:
                    break
                else:
                    current = current.getNext()

        return False

    def add(self , item):
        current = self.head
        prev = None

        while current != None:
            if current.getData() > item:
                break
            else:
                prev = current
                current = current.getNext()

        temp = Node(item)
        if prev == None:
            temp.setnext(self.head)
            self.head = temp
        else:
            temp.setnext(current)
            prev.setnext(temp)     
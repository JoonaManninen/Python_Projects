########################################
#BM40A1500 Data Structures and Algorithms
# Made by: Joona Manninen
# 24.09.2022


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(0)  # Head of the linked list 
        self.tail = self.head  # Tail is the last node
        self.len = 0

    def append(self, data):
             
        newNode = Node(data)
        self.tail.next = newNode  # Append the node
        self.tail = newNode  # Advancing tail
        self.len += 1  # Update the length

    def insert(self, data, indexx):
            
    
        # Making new node
        newNode = Node(data)

        # If index is less than 0 there is incorrect input
        if(indexx < 0):
            return

        elif (indexx == 0):
            temp = self.head
            newNode.next = temp.next
            temp.next = newNode
            self.len += 1  # Update the length
            
        else:     
            temp = self.head
            
            for i in range(0, indexx):
                
                if(temp != None):
                    temp = temp.next   
                    
            if(temp != None):
                newNode.next = temp.next
                temp.next = newNode
                if (indexx == self.len):
                    self.tail = newNode  # Advancing tail
                self.len += 1  # Update the length

    def print (self):
        
        
        temp = self.head
        temp = temp.next
        for i in range(self.len):
            if (i == 0):
                print(temp.value,"",end="")
                temp = temp.next
            elif(i == self.len - 1):
                print("->",temp.value)
            else:
                print("->",temp.value,end=" ")
                temp = temp.next
                
    def index(self, data):
        
        # Using temp variable to store current compared Node
        temp = self.head
        
        indexx = -1
        
        while temp != None:
            if temp.value == data:
                # Returning index number of the value
                return indexx
             
            temp = temp.next
            indexx += 1
        # Returning message if given value didn't match any value in the list
        return -1
    
    def delete(self, indexx):
               
        if (indexx > self.len-1):
            return
        # Using temp variable to store current compared Node
        temp = self.head
        # using other variable to keep track of previous node so the link can be made
        prev = None
        
        num = 0
        
        if (indexx == 0):
            self.head = self.head.next
            self.len -= 1  # Update the length
            return
        
        while (num != indexx):
            temp = temp.next
            prev = temp
            num += 1
        
        if (num == self.len):
            prev.next = None
            self.len -= 1  # Update the length
            return
        
        prev.next = temp.next.next
        self.len -= 1  # Update the length
        return
        
        
if __name__ == "__main__":
    L = LinkedList()
    L.append(1)
    L.append(3)
    L.append(15)
    L.append(2)
    L.print()
    L.append(3)
    L.print()           # 1 -> 3
    L.insert(10, 1)
    L.insert(15, 0)
    L.print()
    L.insert(16, 6)
    L.print()
    L.insert(16, 1)
    L.print()
    L.insert(175, 6)
    L.print()           # 15 -> 1 -> 10 -> 3
    print(L.index(1))   # 1
    L.delete(0)
    L.delete(8)
    L.delete(8)
    L.delete(8)
    L.print()           # 1 -> 10 -> 3
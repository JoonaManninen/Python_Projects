import math
# Open hashtable with chaining.
# Chaining done with linkedlist

# Linkedlist nodes
class Node:
    def __init__(self, key):
        self.val = key
        self.next = None

class HashTable:

    def __init__(self,size):
        # Initializing the hashtable
        self.M = size
        self.T = [None]*self.M
        
        
    # Method used to insert values into the hashtable
    def insert(self, key):
        # Figuring out index number for the key to be stored.
        # Goal is to evenly distripute values in the hashtable
        index = self.hashFunction(key)
        if index == -1:
            print("Unwanted input given.")
            return
           
        
        if self.T[index] == None:
            self.T[index] = Node(key)
        else:
            current = self.T[index]
            while True:
                if current.next == None: 
                    break
                current = current.next
            current.next = Node(key)
        
    # Search method returns true if value is in the hashtable and false if it's not in the hashtable.
    def search(self, key):
        
        # Getting index number so we immediately know where the record is stored.
        index = self.hashFunction(key)
        
        current = self.T[index]
        # Searching 
        while current:
            if current.val == key:
                return True
            else:
                current = current.next
        return False
                        
    # Hash function to hash integers and strings
    def hashFunction(self, key):
        # Using string formatting as the method to hash strings
        if (isinstance(key, str)):
            sum = 0
            multiplier = 1

            N = len(key)
            for i in range(N):
                if (i % 4 == 0):
                    multiplier = 1
                else:
                    multiplier = multiplier * 256
                sum += ord(key[i])*multiplier
            return sum % self.M
        # Using multiplication method to hash integers to get good distribution
        elif(isinstance(key, int)):
            return math.floor(self.M*(float((abs(key)*0.77)) % 1)) % self.M
        # If given value is not integer or string it is invalid 
        else: return -1
    
        # Method which prints the hashtable
    def print(self):
        
        for i in range(self.M):
            
            print(f"|{i}: ",end="")
            
            if (self.T[i] == None): 
                print("")
                continue
            else:
                temp = self.T[i]
                temp1 = temp.next
                while temp is not None:
                    if temp1 is None:
                        print(f"{temp.val}|\n", end="")
                        break
                    else:
                        print(temp.val,"-> ", end="")
                        temp = temp.next
                        temp1 = temp1.next
    
    # Method used when deleting records from the hashtable
    def delete(self, key):
        
        # Getting the key value and figuring index so we immediately know where the record is stored.
        key = self.hashFunction(key)
        index = key % self.M
        
        current = prev = self.T[index]
        if not current: 
            return
        # In case value is in the first slot in the linkedlist
        if current.val == key:
            self.T[index] = current.next
        else:
            current = current.next
            while current:
                # Value found and deleted
                if current.val == key:
                    prev.next = current.next
                    break
                else:
                    # Going through the linkedlist
                    current, prev = current.next, prev.next

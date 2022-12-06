########################################
#BM40A1500 Data Structures and Algorithms
# Made by: Joona Manninen
# 02.10.2022
class HashLinear:
    def __init__(self, M):
        self.M = M              # table size
        self.T = [None] * M     # "empty table"
    
    def insert(self, string):
        # Getting the hash value first
        sum = 0
        num = 0
        N = len(string)
        for i in range(N):
            sum += ord(string[i])
            
        index = sum % self.M # Index which value is put
        
        # Checking that string is not duplicate
        for x in self.T:
            if (x == string):
                return
        # Inserting string to correct index spot
        if self.T[index] == None:
            self.T[index] = string   # Store the integer if the position is free
        else:
            while (num < self.M):
                num = num + 1 # Variable to keep track when every spot has been checked from the hashtable
                if (index == self.M - 1):
                    index = 0 # Setting index to 0 if we are at last index already
                else:
                    index = index + 1
                # Checking if the spot is empty
                if self.T[index] == None:
                    self.T[index] = string
                    break
                
    def delete(self, string):
        
        index = 0
        # Checking that string is in the hash table
        for i in self.T:
            if (i == string):
                self.T[index] = None    # Clearing the hash table index if match was found
            index = index + 1

    def print(self):
        for x in self.T:
            if x == None:
                continue
            else:
                print(f"{x} ", end="")
        print()
        
if __name__ == "__main__":
    table = HashLinear(8)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("10aadfhfdahaaa1")
    table.insert("BM40A1500")
    table.print()   # 10aaaa1 BM40A1500 fOo 123 Bar1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # 10aaaa1 BM40A1500 Bar1
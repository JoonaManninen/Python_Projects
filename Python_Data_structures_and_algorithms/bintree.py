########################################
#BM40A1500 Data Structures and Algorithms
# Made by: Joona Manninen
# 06.10.2022

# Making node we use in BST
class Node:
    def __init__(self, key: int):
        self.val = key
        self.left = None
        self.right = None
 
# BST class where all the functions happen and where data is stored
class BST:
    def __init__(self):
        self.root = None
        
        
        # Function to insert new values to the binary tree
    def insert(self, key):
        return self.help_insert(self.root, key)

    def help_insert(self, node, key):
        # If root doesn't have value we need to give it value.
        if self.root is None:
            self.root = Node(key)
            return
        else:
            # Node value is same as key value so it's discarded because it's already in the bintree
            if node.val == key:
                return
            elif node.val < key:
                # Key value is bigger than node value so it goes to right node.
                if (node.right is None):
                    node.right = Node(key)
                    return
                else:
                    # There is already value in the right node so we move to it with recursion
                    self.help_insert(node.right, key)
            else:
                # Key value is bigger than node value so it goes to left node.
                if (node.left is None):
                    node.left = Node(key)
                    return
                # There is already value in the left node so we move to it with recursion
                else:
                    self.help_insert(node.left, key)    
        return
    # Getting max value from the subtree
    def getmax(self, root):
        if root.right is None: return root
        return self.getmax(root.right)
    # Deleting max value from the subtree
    def deletemax(self, root):
        if root.right is None:
            return root.left
        root.right = self.deletemax(root.right)
        return root
    # Removing node with given key value
    def remove(self, key):
        self.root = self.delete(self.root, key)
        return
    
    def delete(self, rt, key):
        # Checking if the tree is empty
        if rt is None: return None
        if rt.val > key:
            rt.left = self.delete(rt.left, key)
        elif rt.val < key:
            rt.right = self.delete(rt.right, key)
        else: # Found the node
            # Only node on the right
            if rt.left is None: return rt.right    
            # Only node on the right
            elif rt.right is None: return rt.left
            # 2 children nodes
            else:
                temp_node = self.getmax(rt.left)
                rt.val = temp_node.val
                rt.left = self.deletemax(rt.left)
        return rt
            
    # Search function to find if Node is in the binary tree
    def search(self, key):
        return self.search_help(self.root, key)

    # help function for search function
    def search_help(self, node, key):
        
        if not node:
            return False
        elif node.val > key:
            return self.search_help(node.left, key)
        elif node.val < key:
            return self.search_help(node.right, key)
        # if None of the conditions were true. Means that the Node stores the value
        return True

    def preorder(self):
        # List where node values are stored
        list = []

        self.preorderHelp(self.root, list)
        
        # Printing list
        for i in list:
            print(i, end=" ")
            
        print()    
        return

    def preorderHelp(self, node, list):

        if node is None:
            return 
        # Adding Node value to the list
        list.append(node.val)

        # Calling recursively preorderhelp so we can go through all the Nodes
        self.preorderHelp(node.left, list)
        self.preorderHelp(node.right, list)
        
        return

if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 4, 6, 2]
    for key in keys:
        Tree.insert(key)

    Tree.preorder()     # 5 1 3 2 4 9 7 6 
    Tree.remove(1)
    Tree.preorder()     # 5 3 2 4 9 7 6 
    Tree.remove(9)
    Tree.preorder()     # 5 3 2 4 7 6
    Tree.remove(3)
    Tree.preorder()     # 5 2 4 7 6
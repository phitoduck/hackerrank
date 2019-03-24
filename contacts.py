# To count the number of words beginning with a specified prefix,
# I implemented a Trie

numOperations = int(input())

contacts = list()

class Tree:
    def __init__(self):
        self.root = Node('.')
    
    def find(self, word):
        current_node = self.root
        for char in word:
            if char in current_node.children.keys():
                current_node = current_node.children[char]
            else:
                return 0
        return current_node.count
    
    def add_word(self, word):
        current_node = self.root
        for char in word:
            current_node.update(char)
            current_node = current_node.children[char]
            
    
class Node:
    def __init__(self, value):
        self.value = value
        self.children = dict()
        self.count = 1
    
    def update(self, letter):
        if letter not in self.children.keys():
            self.children[letter] = Node(letter)
        else:
            self.children[letter].count += 1

            
tree = Tree()
for _ in range(numOperations):
    operation, name = input().split()
    
    numMatches = 0
    if operation == "add":
        tree.add_word(name)
    else:
        print(tree.find(name))

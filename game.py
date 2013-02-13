


# trie node
class Node:
    def __init__(self, letter, parent):
        self.letter = letter
        self.parent = parent
        self.children = {}
        

words = open('wordlist.txt').readlines()
print len(words)
    

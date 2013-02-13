


# trie node
class Node:
    def __init__(self, letter, parent):
        self.letter = letter
        self.parent = parent
        self.children = {}
        self.isEnd = False
    def process_word(self, word):
        if len(word) == 0:
            self.isEnd = True
            return
        
        next_letter = word[0]
        if next_letter not in self.children:
            self.children[next_letter] = Node(next_letter, self)
        self.children[next_letter].process_word(word[1:])

# class to manage game
class Game:
    def __init__(self):
        self.root = Node(None, None)
        for line in open('wordlist.txt').readlines():
            self.root.process_word(line.strip())
        

game = Game()



import random

# trie node
class Node:
    def __init__(self, letter, parent):
        self.letter = letter
        self.parent = parent
        self.children = {}
        self.isWordEnd = False
        self.isGoodMove = True
        
        self.depth = 0
        if parent is not None:
            self.depth = parent.depth + 1

    # reads in (the remainder of) a word and expands the trie as necessary
    def process_word(self, word):
        if len(word) == 0:
            self.isWordEnd = True
            self.isGoodMove = False
            self.parent.updateGood()
            return
        
        next_letter = word[0].upper()
        if next_letter not in self.children:
            self.children[next_letter] = Node(next_letter, self)
        self.children[next_letter].process_word(word[1:])

    # sets self.isGoodMove to True if choosing the letter this node represents is a winning move
    # also sets isGoodMove appropriately for parent Nodes
    def updateGood(self):
        if self.isWordEnd:
            return
        
        if any([self.children[c].isGoodMove for c in self.children]):
            self.isGoodMove = False
        else:
            self.isGoodMove = True

        if self.parent is not None:
            self.parent.updateGood()

    def getNode(self, word):
        if len(word) == 0:
            return self
        next_letter = word[0].upper()
        if next_letter not in self.children:
            return None
        return self.children[next_letter].getNode(word[1:])

    # randomly picks a way to travel to a leaf
    def example_completion(self):
        nexts = list(self.children.keys())
        if len(nexts) == 0:
            return self.letter
        return self.letter + self.children[random.choice(nexts)].example_completion()

class Game:

    MAX_OK_WORD = 3
    EASY_MODE_SEARCH_TRIES = 1
    HARD_MODE_SEARCH_TRIES = 6
    YN_RESPONSE_DICT = {}
    LETTER_RESPONSE_DICT = {}
    
    def __init__(self):
        print "========== WORDTRAIN =========="
        print "beep boop beep boop beep beep boop boop"
        self.load_dictionary()
        self.setup_response_dicts()
        self.print_rules()

        print ""
        if self.prompt("Would you like to play on hard mode? (Y/N) ", Game.YN_RESPONSE_DICT):
            self.search_tries = Game.HARD_MODE_SEARCH_TRIES
        else:
            self.search_tries = Game.EASY_MODE_SEARCH_TRIES
        
    def start(self):        
        self.current_node = self.root
        self.current_letters = ""

        print ""
        
        if self.prompt("Would you like to go first? (Y/N) ", Game.YN_RESPONSE_DICT):
            self.finish(self.human_move())
        else:
            self.finish(self.computer_move())

    def finish(self, human_wins):
        if human_wins:
            print "==========  YOU WIN  =========="
        else:
            print "========== GAME OVER =========="
        if self.prompt("Play again? (Y/N) ", Game.YN_RESPONSE_DICT):
            self.start()

    # returns True if the human wins
    def human_move(self):
        letter = self.prompt("Type in a letter: " + self.current_letters, Game.LETTER_RESPONSE_DICT)

        if letter not in self.current_node.children:
            print "Ha! No word of acceptable length begins with " + self.current_letters + letter + "!"
            print "You could have gone for " + self.current_letters + self.current_node.example_completion()[1:] + "."
            return False

        self.current_node = self.current_node.children[letter]
        self.current_letters += letter

        if self.current_node.isWordEnd and self.current_node.depth > Game.MAX_OK_WORD:
            print "Uh-oh, you made a word!"
            return False
        
        return self.computer_move()

    # returns True if the human wins
    def computer_move(self):

        for i in range(self.search_tries):
            letter = random.choice(list(self.current_node.children.keys()))
            if self.current_node.children[letter].isGoodMove:
                break

            
        self.current_node = self.current_node.children[letter]
        self.current_letters += letter

        #     "Type in a letter: "
        print "OK. My move:      " + self.current_letters

        if self.current_node.isWordEnd and self.current_node.depth > Game.MAX_OK_WORD:
            print "Oops, I made a word!"
            return True
        if len(self.current_node.children) == 0:
            print "Oops, there's no way to make a longer word out of that."
            return True
        
        return self.human_move()

    def print_rules(self):
        print ""
        print "Rules: We will take turns adding letters to the train."
        print "At any point in time, the letters must be the beginning"
        print "of a word longer than " + str(Game.MAX_OK_WORD) +  ". However, the first to "
        print "complete a word longer than " + str(Game.MAX_OK_WORD) + " letters loses."
        
    def load_dictionary(self):
        self.root = Node(None, None)
        print "Loading dictionary..."
        for line in open('wordlist.txt').readlines():
            word = line.strip()
            if len(word) > Game.MAX_OK_WORD and word.isalpha() and not word.isupper():
                self.root.process_word(word)
        print "Dictionary loaded."

    # used for prompts to the user
    # the response_dicts map possible responses to interpretations
    def setup_response_dicts(self):
        Game.YN_RESPONSE_DICT = {}
        Game.LETTER_RESPONSE_DICT = {}

        for s in ["Yes","Y","YES","yes","y"]:
            Game.YN_RESPONSE_DICT[s] = True
        for s in ["No","N","NO","no","n"]:
            Game.YN_RESPONSE_DICT[s] = False
        for s in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            Game.LETTER_RESPONSE_DICT[s] = s.upper()
        

    # prompts user
    def prompt(self, text, response_dict):
        
        while True:
            response = raw_input(text)
            if response in response_dict:
                break
            else:
                print "I don't understand what you mean."
        return response_dict[response]

game = Game()
game.start()

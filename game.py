
import random

# trie node
class Node:
    def __init__(self, letter, parent):
        self.letter = letter
        self.parent = parent
        self.children = {}
        self.isEnd = False
        self.isGoodMove = True
        
        self.depth = 0
        if parent != None:
            self.depth = parent.depth + 1
        
    def process_word(self, word):
        if len(word) == 0:
            self.isEnd = True
            self.setGood(False)
            return
        
        next_letter = word[0].upper()
        if next_letter not in self.children:
            self.children[next_letter] = Node(next_letter, self)
        self.children[next_letter].process_word(word[1:])

    def setGood(self, isGood):
        if not isGood:
            self.isGoodMove = False
        if not self.isGoodMove:
            return
        if self.parent is not None:
            self.parent.setGood(not isGood)
        

    def example_completion(self):
        nexts = list(self.children.keys())
        if len(nexts) == 0:
            return self.letter
        return self.letter + self.children[random.choice(nexts)].example_completion()

# class to manage game
class Game:

    MAX_OK_WORD = 3
    YN_RESPONSE_DICT = {}
    LETTER_RESPONSE_DICT = {}
    
    def __init__(self):
        print "========== WORDTRAIN =========="
        print "beep boop beep boop beep beep boop boop"
        self.load_dictionary()
        self.setup_response_dicts()
        self.print_rules()
        


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

    def human_move(self):
        letter = self.prompt("Type in a letter: " + self.current_letters, Game.LETTER_RESPONSE_DICT)

        if letter not in self.current_node.children:
            print "Ha! No word of acceptable length begins with " + self.current_letters + letter + "!"
            print "You could have gone for " + self.current_letters + self.current_node.example_completion()[1:] + "."
            return False

        self.current_node = self.current_node.children[letter]
        self.current_letters += letter

        if self.current_node.isEnd and self.current_node.depth > Game.MAX_OK_WORD:
            print "Uh-oh, you made a word!"
            return False
        
        return self.computer_move()
        
    def computer_move(self):
        letter = random.choice(list(self.current_node.children.keys()))
        self.current_node = self.current_node.children[letter]
        self.current_letters += letter

        #     "Type in a letter: "
        print "OK. My move:      " + self.current_letters

        if self.current_node.isEnd and self.current_node.depth > Game.MAX_OK_WORD:
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
        print "of some English word. However, the first player to "
        print "complete a word longer than " + str(Game.MAX_OK_WORD) + " letters loses."
        

    def load_dictionary(self):
        self.root = Node(None, None)
        print "Loading dictionary..."
        for line in open('wordlist.txt').readlines():
            word = line.strip()
            if len(word) > Game.MAX_OK_WORD:
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

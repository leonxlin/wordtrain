


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
        print "========== WORDTRAIN =========="
        print "beep boop beep boop beep beep boop boop"
        self.load_dictionary()
        self.setup_response_dicts()

    def start(self):
        if self.prompt("Would you like to go first? (Y/N) ", self.yn_response_dict):
            self.human_move()
        else:
            self.computer_move()

    def human_move(self):
        pass
    def computer_move(self):
        pass

    def load_dictionary(self):
        self.root = Node(None, None)
        print "Loading dictionary..."
        for line in open('wordlist.txt').readlines():
            self.root.process_word(line.strip())
        print "Dictionary loaded."

    # used for prompts to the user
    # the response_dicts map possible responses to interpretations
    def setup_response_dicts(self):
        self.yn_response_dict = {}
        self.letter_response_dict = {}

        for s in ["Yes","Y","YES","yes","y"]:
            self.yn_response_dict[s] = True
        for s in ["No","N","NO","no","n"]:
            self.yn_response_dict[s] = False
        for s in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            self.letter_response_dict[s] = s.lower()
        

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




# trie node
class Node:
    def __init__(self, letter, parent):
        self.letter = letter
        self.parent = parent
        self.children = {}
        self.isEnd = False
        
        self.depth = 0
        if parent != None:
            self.depth = parent.depth + 1
        
    def process_word(self, word):
        if len(word) == 0:
            self.isEnd = True
            return
        
        next_letter = word[0].upper()
        if next_letter not in self.children:
            self.children[next_letter] = Node(next_letter, self)
        self.children[next_letter].process_word(word[1:])

# class to manage game
class Game:

    MAX_OK_WORD = 3
    
    def __init__(self):
        print "========== WORDTRAIN =========="
        print "beep boop beep boop beep beep boop boop"
        self.load_dictionary()
        self.setup_response_dicts()
        self.print_rules()
        
        self.current_node = self.root
        self.current_letters = ""


    def start(self):        

        if self.prompt("Would you like to go first? (Y/N) ", self.yn_response_dict):
            self.finish(self.human_move())
        else:
            self.finish(self.computer_move())

    def finish(self, human_wins):
        pass
        

    def human_move(self):
        letter = self.prompt("Type in a letter: " + self.current_letters, self.letter_response_dict)

        if letter not in self.current_node.children:
            print "Ha! No word begins with " + self.current_letters + letter + "!"
            return False

        self.current_node = self.current_node
        return self.computer_move()
        
    def computer_move(self):


        
        #      Type in a letter: 
        print "OK. My move:      "
        return False

    def print_rules(self):
        print "Rules: We will take turns adding letters to the train."
        print "At any point in time, the letters must be the beginning"
        print "of some English word. However, the first player to"
        print "complete a word longer than " + str(Game.MAX_OK_WORD) + " letters loses."
        

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
            self.letter_response_dict[s] = s.upper()
        

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

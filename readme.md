
Wordtrain is a simple word game, certainly not invented by me.

How to play
----

Download the files, open the directory in a terminal window, and run `python game.py`.

Players take turns saying letters. The sequence of any letters at any time must correspond to the beginning of a word longer than three letters.

Whichever player is first forced to complete a word longer than three letters loses.

About
----

The program stores the contents of a list of English words in a trie. The list, `wordlist.txt`, is from [SIL International](http://www.sil.org/linguistics/wordlists/english/). The program also determines a winning strategy for every possible stage in the game. This information is used by the program in hard mode, though there is an element of chance — even in hard mode, the program may not choose the best move each turn.

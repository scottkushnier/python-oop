"""Word Finder: finds random words from a dictionary."""

from random import choice, randint, seed

class WordFinder:

    """ structure:  
       wordlist
       size  (how many words in wordlist)

                    >>> w = WordFinder('words.txt')

                    >>> seed(42)

                    >>> randint(1,100)
                    82
                    
                    >>> w.random()
                    'calyx'

                    >>> w.random()
                    'ameloblastic'

                    >>> w.random()
                    'superevident'

                    >>> w2 = SpecialWordFinder('words-3.txt')

                    >>> w2.random()
                    'bird'

                    >>> w2.random()
                    'dog'

                    >>> w2.random()
                    'dog'


                    

    """

    def __init__(self, word_file):
        """WordFind object is initialized by reading a list of words from a file & storing those words away in a list"""
        words = []
        file = open(word_file, "r")
        for word in file:
            if len(word) > 2:
                words.append(word.strip())
        file.close()
        self.wordlist = words
        self.size = len(words)

    def random(self):
        """ return a random word from the word list"""
        return choice(self.wordlist)


class SpecialWordFinder(WordFinder):

    """ just like WordFinder, but ignores blank lines & comment lines
    """

    def __init__(self, word_file):
        """WordFind object is initialized by reading a list of words from a file & storing those words away in a list"""
        super().__init__(word_file)
        for word in self.wordlist:
            if word[0] == '#':
                self.wordlist.remove(word)
        self.size = len(self.wordlist)
    

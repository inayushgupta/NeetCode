class Node:
    def __init__(self, letter):
        self.letter = letter
        self.ending = False
        self.pointers = [None] * 26

        
def letter_index(letter: str) -> int:
    return ord(letter) - ord('a')


class PrefixTree:

    def __init__(self):
        self.trie = Node(' ')

    def insert(self, word: str) -> None:

        curr = self.trie

        for letter in word:
            index = letter_index(letter)
            if not curr.pointers[index]:
                curr.pointers[index] = Node(letter)
            curr = curr.pointers[index]
        
        curr.ending = True
            

    def search(self, word: str) -> bool:

        curr = self.trie

        for letter in word:
            index = letter_index(letter)
            if not curr.pointers[index]:
                return False
            curr = curr.pointers[index]
        
        return curr.ending
        

    def startsWith(self, prefix: str) -> bool:

        curr = self.trie
        
        for letter in prefix:
            index = letter_index(letter)
            if not curr.pointers[index]:
                return False
            curr = curr.pointers[index]
        
        return True
        
        
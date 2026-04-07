def get_index(letter):
    return ord(letter) - ord('a')

class Node:
    def __init__(self, letter):
        self.letter = letter
        self.ending = False
        self.pointers = [None] * 26

class WordDictionary:

    def __init__(self):
        self.trie = Node(' ')

    def addWord(self, word: str) -> None:
        
        curr = self.trie

        for letter in word:
            index = get_index(letter)
            if not curr.pointers[index]:
                curr.pointers[index] = Node(letter)
            curr = curr.pointers[index]
            
        curr.ending = True

    def search(self, word: str) -> bool:
        
        def helper(node, index):

            if not node:
                return False
            
            if len(word) == index:
                return node.ending
            
            letter = word[index]
            if letter == '.':
                res = False
                for pointer in node.pointers:
                    res = res or helper(pointer, index+1)
                return res

            letter_index = ord(letter) - ord('a')
            pointer_value = node.pointers[letter_index]

            if pointer_value:
                return helper(pointer_value, index+1)
            return False

        return helper(self.trie, 0)



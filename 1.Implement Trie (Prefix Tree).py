problem link : https://leetcode.com/problems/implement-trie-prefix-tree/description/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endsWith = False

    def containKey(self, ch):
        return self.children[ord(ch)-ord('a')] != None

    def put(self, ch, children):
        self.children[ord(ch)-ord('a')] = children

    def get(self, ch):
        return self.children[ord(ch)-ord('a')]

    def setEnd(self):
        self.endsWith = True

    def isEnd(self):
        return self.endsWith

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if curr.containKey(ch) == False:
                curr.put(ch, TrieNode())
            curr = curr.get(ch)
        curr.setEnd()

    def search(self, word):
        curr = self.root
        for ch in word:
            if not curr.containKey(ch):
                return False 
            curr = curr.get(ch)
        return curr.isEnd()

    def startsWith(self, prefix):
        curr = self.root
        for ch in prefix:
            if not curr.containKey(ch):
                return False 
            curr = curr.get(ch)
        return True  
        
''' time complexity : O(l) - l max lenght of words
    space complexity : O(n * 26) - (n = total characters in all words inserted)
'''


########################################################################################################################################################################################################
# use dictionary instead of a array 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endsWith = False

    def containKey(self, ch):
        return ch in self.children

    def put(self, ch, children):
        self.children[ch] = children

    def get(self, ch):
        return self.children[ch]

    def setEnd(self):
        self.endsWith = True

    def isEnd(self):
        return self.endsWith

''' time complexity : O(l) - l max lenght of words
    space complexity : O(n) - (n = total characters in all words inserted)
'''

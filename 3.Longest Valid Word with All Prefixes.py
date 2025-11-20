problem link : https://www.geeksforgeeks.org/problems/longest-valid-word-with-all-prefixes/1

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endsWith = False 
    
    def containsKey(self, ch):
        return ch in self.children
    
    def get(self, ch):
        return self.children[ch]
    
    def put(self, ch, node):
        self.children[ch] = node
    
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
            if not curr.containsKey(ch):
                curr.put(ch, TrieNode())
            curr = curr.get(ch)
        curr.setEnd()
    
    def containAllPrefix(self, word):
        curr = self.root
        for ch in word:
            if curr.containsKey(ch):
                curr = curr.get(ch)
                if not curr.isEnd():
                    return False 
            else:
                return False 
        return True

class Solution:
    def longestValidWord(self, words):
        trie = Trie()
        
        for word in words:
            trie.insert(word)
            
        longest_word = ""
        for word in words:
            if trie.containAllPrefix(word):
                if len(longest_word) < len(word):
                    longest_word = word
                elif len(longest_word) == len(word) and word < longest_word:
                    longest_word = word
        return longest_word
        

''' 
    time complexity : O(n * l)
    space complexity : O(n * l)
    n - number of words in words
    l - maximum length of a word
'''


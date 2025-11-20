problem link : https://www.naukri.com/code360/problems/implement-trie_1387095

from os import *
from sys import *
from collections import *
from math import *

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.postfixCount = 0
        self.prefixCount = 0 
    
    def containsKey(self, ch):
        return ch in self.children
    
    def increasePostfix(self):
        self.postfixCount += 1
    
    def decreasePostfix(self):
        self.postfixCount -= 1
    
    def increasePrefix(self):
        self.prefixCount += 1
    
    def decreasePrefix(self):
        self.prefixCount -= 1
    
    def getChildNode(self, ch):
        return self.children[ch] 
    
    def putChildNode(self, ch, node):
        self.children[ch] = node 

    def getPrefixCount(self):
        return self.prefixCount

    def getPostfixCount(self):
        return self.postfixCount    

class Trie:
    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word):
        curr = self.root 
        for ch in word:
            if not curr.containsKey(ch):
                curr.putChildNode(ch, TrieNode())
            
            curr = curr.getChildNode(ch)
            curr.increasePrefix()
        curr.increasePostfix()        

    def countWordsEqualTo(self, word):
        curr = self.root 
        for ch in word:
            if not curr.containsKey(ch):
                return 0            
            curr = curr.getChildNode(ch)           
        return curr.getPostfixCount()

    def countWordsStartingWith(self, word):
        curr = self.root 
        for ch in word:
            if not curr.containsKey(ch):
                return 0
            
            curr = curr.getChildNode(ch)            
        return curr.getPrefixCount()

    def erase(self, word):
        curr = self.root 
        for ch in word:
            if not curr.containsKey(ch):
                return 0
            
            curr = curr.getChildNode(ch)            
            curr.decreasePrefix()
        curr.decreasePostfix()


''' time complexity : O(l) - l max lenght of words
    space complexity : O(n) - (n = total characters in all words inserted)
'''

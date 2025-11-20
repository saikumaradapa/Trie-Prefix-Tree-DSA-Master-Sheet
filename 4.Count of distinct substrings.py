problem link : https://www.geeksforgeeks.org/problems/count-of-distinct-substrings/1

class TrieNode:
    def __init__(self):
        self.children = dict()

    def containsKey(self, ch):
        return ch in self.children
    
    def get(self, ch):
        return self.children[ch]
    
    def put(self, ch, node):
        self.children[ch] = node

def countDistinctSubstring(s):
    root = TrieNode()
    
    cnt = 0
    for i in range(len(s)):
        curr = root
        for j in range(i, len(s)):
            if not curr.containsKey(s[j]):
                cnt += 1
                curr.put(s[j], TrieNode())
            curr = curr.get(s[j])
    return cnt + 1

''' There is a more space/time efficient method using Suffix Automaton or Suffix Trie/Tree
    time complexity : O(n ^ 2)
    space complexity : O(n ^ 2)
    n - length of the string
'''


'''
https://leetcode.com/problems/implement-trie-prefix-tree/
->Tree data structure used to efficiently store and retrieve keys in a dataset of strings.
->There are several other data structures, like balanced trees and hash tables, which give us
the possibility to search for a word in a dataset of strings. Then why do we need trie?
      hashtables cannot be used to search for all keys with a common prefix
      lexicographical order??



'''


class Trie_node:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = Trie_node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie_node()  # insert letter as a link in the tree
            cur = cur.children[c]

        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)aram_3 = obj.startsWith(prefix)
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        trie = self.root

        for i in word:
            # if the letter is not in the trie, then add it as a child
            if i not in trie:
                trie[i] = {}

            # enter child node
            trie = trie[i]
        print(trie)

        # mark end of the word
        trie[None] = None
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self.root

        for i in word:
            if i not in trie:
                return False
            trie = trie[i]

        if None in trie:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self.root
        
        for i in prefix:
            if i not in trie:
                return False

            trie = trie[i]
        return True


trie = Trie()

trie.insert("apple")
print(trie.search("apple"))   # returns True
print(trie.search("app"))     # returns False
print(trie.startsWith("app")) # returns True
trie.insert("app")
print(trie.search("app"))     # returns True
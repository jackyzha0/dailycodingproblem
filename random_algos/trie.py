class TrieNode():
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isEndOfWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode("root")

    def add(self, word):
        root = rootref = self.root

        for c in word:
            if not c in root.children:
                root.children[c] = TrieNode(c)
            root = root.children[c]

        root.isEndOfWord = True
        self.root = rootref

    def search(self, word):
        root = self.root
        for c in word:
            if c in root.children:
                root = root.children[c]
            else:
                return False

        if root.isEndOfWord:
            return True
        else:
            return False

T1 = Trie()
T1.add("asdf")
T1.add("yeet")
T1.add("yeetya")

assert T1.search("asdf")
assert not T1.search("asd")
assert not T1.search("y")
assert T1.search("yeet")
assert T1.search("yeetya")
assert not T1.search("yeetasdf")

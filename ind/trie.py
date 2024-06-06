class Node:
    def __init__(self):
        self.children = dict()
        self.word_end = False


class Trie:
    def __init__(self):
        self.node = Node()

    def insert(self, s: str):
        curr = self.node
        for ch in s:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.word_end = True

    def search(self, s: str) -> bool:
        curr = self.node
        for ch in s:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False
        return curr.word_end


if __name__ == '__main__':
    words = ['abc', 'ab', 'cdf', 'adc']

    t = Trie()
    for wd in words:
        t.insert(wd)

    for wd in words + ['cde', 'cd']:
        print(wd, t.search(wd))

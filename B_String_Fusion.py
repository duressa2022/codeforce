class TrieNode:
    def __init__(self):
        self.children = {}
        self.sum = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.result = 0

    def insert(self, word):
        node = self.root
        node.sum += 1
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sum += 1

    def update(self, word):
        current_length = len(word)
        node = self.root
        for char in word:
            if char not in node.children:
                self.result += node.sum * current_length
                break
            else:
                next_node = node.children[char]
                self.result += (node.sum - next_node.sum) * current_length
                current_length -= 1
                node = next_node

def solve(n, words):
    total_size = sum(len(word) for word in words)
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    for word in words:
        reversed_word = word[::-1]
        trie.update(reversed_word)
    
    return trie.result

def mainSolver():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    words = data[1:n + 1]
    
    result = 0
    result += solve(n, words)
    words = [word[::-1] for word in words]  
    result += solve(n, words)
    
    print(result)

mainSolver()

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self): 
        self.root = TrieNode()
    
    def insert(self, word):
        cur=self.root
        for char in word:
            if char not in cur.children:
                cur.children[char]=TrieNode()
            cur=cur.children[char]
        cur.is_end=True
    
    def is_prefix(self, word):
        cur=self.root
        for char in word:
            if char in cur.children:
                cur=cur.children[char]
                if cur.is_end:
                    return True
            else:
                return False
        return True
def generate_binary(length,current,results):
    if length==len(current):
        results.append(current)
        return 
    generate_binary(length,current+"0",results)
    generate_binary(length,current+"1",results)

def solver(n, lengths):
    lengths.sort()
    trie = Trie()
    words = []
    
    for length in lengths:
        possible_words = []
        generate_binary(length, '', possible_words)
        
        flag = False
        for word in possible_words:
            if not trie.is_prefix(word):
                trie.insert(word)
                words.append(word)
                flag = True
                break
        
        if not flag:
            return "NO"
    
    result = "YES\n" + "\n".join(words)
    return result
n = int(input())
lengths = list(map(int, input().split()))
print(solver(n, lengths))

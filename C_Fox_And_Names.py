from collections import defaultdict,deque
def solver():
    length=int(input())
    words=[]
    for _ in range(length):
        words.append(input())
    graph=defaultdict(list)
    for i in range(length-1):
        word1=words[i]
        word2=words[i+1]
        minlength=min(len(word1),len(word2))
        if word1[:minlength]==word2[:minlength] and len(word1)>len(word2):
            return "Impossible"
        for j in range(minlength):
            if word1[j]!=word2[j]:
                graph[word1[j]].append(word2[j])
                break
    visted={}
    order=[]
    def dfs(node):
        if node in visted:
            return visted[node]
        visted[node]=True
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        visted[node]=False
        order.append(node)
        return False
    nodes=[]
    for char in graph:
        nodes.append(char)
    for node in nodes:
        if dfs(node):
            return "Impossible"
    return "".join(list(reversed(order)))
result=solver()
if result=="Impossible":
    print(result)
else:
    correct="abcdefghijklmnopqrstuvwxyz"
    temp=result
    time=set(result)
    result=[]
    for char in correct:
        if char not in time:
            result.append(char)
    for char in temp:
        result.append(char)
    print("".join(result))


from collections import Counter
def solve(word):
    n = len(word)
    order = []
    s = set()
    for i in range(n-1, -1, -1):
        if not word[i] in s:
            order.append(word[i])
        s.add(word[i])
    order.reverse()
    c = Counter(word)
    original_count = Counter()
    for j in range(len(order)):
        original_count[order[j]] = c[order[j]] // (j+1)
    
    i = 0
    curr_count = Counter()
    while i < n and curr_count != original_count:
        curr_count[word[i]] += 1
        i += 1
    original_string = word[:i]

    word_list = [l for l in original_string]
    prev_string  = [l for l in original_string]
    for i in range(len(order)):
        cur_substr = [l for l in prev_string if l != order[i]]
        word_list.extend(cur_substr)
        prev_string = cur_substr
    if "".join(word_list) == word:
        print(original_string + " "+ "".join(order))
    else:
        print(-1)
        
for _ in range(int(input())):
    solve(input())
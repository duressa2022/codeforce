def functionHelper(string):
    stack=[-1]
    length=[]
    maxLength=-float("inf")
    for i,char in enumerate(string):
        if char=="(":
            stack.append(i)
        else:
            if stack:
                current=i-stack[-1]
                maxLength=max(maxLength,current)
                length.append(current)
            else:
                stack.append(i)
    lengthCount={lenValue:length.count(lenValue) for lenValue in length}
    if maxLength==-float("inf"):
        return (0,1)
    else:
        return (maxLength,lengthCount[maxLength])
from collections import Counter
def find_longest_regular_bracket_sequence(s):
    stack = [-1]
    valid_lengths = []
    max_len = float('-inf')

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                current_len = i - stack[-1]
                max_len = max(max_len, current_len)
                valid_lengths.append(current_len)
            else:
                stack.append(i)
    length_counts = Counter(valid_lengths)
    if max_len == float('-inf'):
        return (0, 1)
    else:
         return (max_len, length_counts[max_len])

s = input()
max_length, num_sequences = find_longest_regular_bracket_sequence(s)
print(max_length, num_sequences)


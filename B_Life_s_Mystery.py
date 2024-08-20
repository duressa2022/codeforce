string=input()
stack=[]
hashset=set()
for char in  string:
    if stack and stack[-1]==char:
        while stack and stack[-1]==char:
            stack.pop()
        continue
    stack.append(char)
print("".join(stack))


from collections import deque
def solver(string):
    length=len(string)
    queue=deque([])
    if length%2==1:
        flag=True
        for char in string:
            if flag==True:
                queue.append(char)
                flag=False
            else:
                queue.appendleft(char)
                flag=True
    else:
        flag=True
        queue.append(string[0])
        for index in range(1,length):
            if flag==True:
                queue.append(string[index])
                flag=False
            else:
                queue.appendleft(string[index])
                flag=True
    return "".join(queue)

n=input()
string=input()
ans=solver(string)
print(ans)
                
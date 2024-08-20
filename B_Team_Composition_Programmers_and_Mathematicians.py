from collections import defaultdict,deque
def solver(skills,k):
    n=len(skills)
    queue=deque(skills)
    counter=0
    score=defaultdict(int)
    while counter<k:
        x=queue.popleft()
        y=queue.popleft()
        if x>y:
            score[x]+=1
            queue.append(y)
            queue.appendleft(x)
        else:
            queue.append(x)
            score[y]+=1
            queue.appendleft(y)
        counter+=1
    for key in score:
        if score[key]==k:
            return key
ans=solver([2,5,4],3)
print(ans)
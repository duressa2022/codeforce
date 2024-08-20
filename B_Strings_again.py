from collections import deque
for _ in range(int(input())):
    n,m,k=list(map(int,input().split()))
    queue1=deque(sorted([char for char in input()]))
    queue2=deque(sorted([char for char in input()]))
    queue=deque()
    counter1=0
    counter2=0
    while queue1 and queue2:
        if queue1[0]<queue2[0]:
            if counter1<k:
                queue.append(queue1.popleft())
                counter2=0
                counter1+=1
            else:
                queue.append(queue2.popleft())
                counter1=0
                counter2+=1
        else:
            if counter2<k:
                queue.append(queue2.popleft())
                counter1=0
                counter2+=1
            else:
                queue.append(queue1.popleft())
                counter1+=1
                counter2=0
    print("".join(queue))


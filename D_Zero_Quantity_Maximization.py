from collections import defaultdict
from fractions import Fraction


length = int(input()) 
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split())) 
myCounter = defaultdict(int) 
counter = 0   
for i in range(length):
    if list2[i] == 0 and list1[i] == 0:
            counter+= 1
    elif list1[i]:
            fraction = Fraction(-list2[i], list1[i])
            myCounter[fraction] += 1
        
counter += max(myCounter.values()) if myCounter else 0
print(counter)


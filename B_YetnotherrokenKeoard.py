t=int(input())
for i in range(t):
    word=input()
    smallest_tracker=[]
    capital_tracker=[]
    result=[]
    for char in word:
        if char=="B":
            if capital_tracker:
                result[capital_tracker.pop()]=""
        elif char=="b":
            if smallest_tracker:
                result[smallest_tracker.pop()]=""
        else:
            if char.islower():
                smallest_tracker.append(len(result))
            else:
                capital_tracker.append(len(result))
            result.append(char)
    print("".join(result))
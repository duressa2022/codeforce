for _ in range(int(input())):
    chars={char:index+1 for index,char in enumerate(input())}
    word=input()
    time=0
    for index in range(1,len(word)):
        time+=abs(chars[word[index]]-chars[word[index-1]])
    print(time)
t=int(input())
for i in range(t):
    n = int(input())
    s = input()

    left = 0
    right = n
    while left < right and s[left] == s[right - 1]:
        left += 1
        right -= 1
    if left >= right:
        print("Yes")
        continue
    while left < right and s[left] != s[right - 1]:
        left += 1
        right -= 1
    while left < right and s[left] == s[right - 1]:
        left += 1
        right -= 1
    if left >= right:
        print("Yes")
    else:
        print("No")

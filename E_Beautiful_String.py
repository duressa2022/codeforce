n, k = map(int, input().split())
s = input()

left = 0
b = 0
max_length = 1
for right in range(n):
    if s[right] == 'b':
        b += 1
    while b > k:
        if s[left] == 'b':
            b -= 1
        left += 1

    max_length = max(max_length, right - left + 1)
left = 0
a = 0

for right in range(n):
    if s[right] == 'a':
        a += 1
    while a > k:
        if s[left] == 'a':
            a -= 1
        left += 1
    max_length = max(max_length, right - left + 1)
print(max_length)
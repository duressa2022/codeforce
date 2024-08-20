for _ in range(int(input())):
    n = int(input())
    lines = input()
    values = []
    totCount = 0
    for i, line in enumerate(lines):
        if line == 'L':
            totCount += i
            values.append(max(i, n - i - 1) - i)
        else:
            totCount += (n - i - 1)
            values.append(max(i, n - i - 1) - (n - i - 1))
    values.sort(reverse=True)
    for i in range(len(values)):
        totCount += values[i]
        values[i] = totCount
    
    print(*values)

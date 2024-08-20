def solver(a, z):
  max_value = max(a)
  for i in range(len(a)):
    a[i] |= z
    max_value = max(max_value, a[i])
    z &= a[i]
  return max_value

t = int(input())
for _ in range(t):
  n, z = map(int, input().split())
  a = list(map(int, input().split()))
  result = solver(a, z)
  print(result)

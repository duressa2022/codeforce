def solver(left, right, array):
    if right - left == 1:
        return 0
    mid = (left + right) // 2
    left_max = max(array[left:mid])
    right_max = max(array[mid:right])
    ans = 0
    if left_max > right_max:
        ans += 1
        array[left:mid], array[mid:right] = array[mid:right], array[left:mid]
    return solver(left, mid, array) + solver(mid, right, array) + ans

def main():
    t = int(input())
    for _ in range(t):
        m = int(input())
        arr = list(map(int, input().split()))
        ans = solver(0, m, arr)
        if arr == sorted(arr):
            print(ans)
        else:
            print(-1)

if __name__ == "__main__":
    main()

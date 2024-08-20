def main():
    length = int(input())
    array=[0]+[int(num) for num in input().split()]+[1001]
    result = 0
    counter = 0
    for i in range(1, length + 1):
        if array[i] == array[i - 1] + 1 and array[i] == array[i + 1] - 1:
            counter += 1
            result = max(result, counter)
        else:
            counter = 0
    print(result)
main()
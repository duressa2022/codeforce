from collections import defaultdict

test_cases=int(input())
for _ in range(test_cases):
    array_length = int(input())
    array = list(map(int, input().split()))

    count_dict = defaultdict(int)
    appearance_dict = defaultdict(int)

    for element in array:
        count_dict[element] += 1
        current_count = count_dict[element]
        appearance_dict[current_count] += current_count

    max_appearance = max(appearance_dict.values())

    print(array_length - max_appearance)
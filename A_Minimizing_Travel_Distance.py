value_list=[int(value) for value in input().split()]
value_list.sort()
print(value_list[1]-value_list[0]+value_list[2]-value_list[1])
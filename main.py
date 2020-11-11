list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
print(list_to_sort)
sorted_list = sorted(list_to_sort, key=lambda x: (x[1], x[2])) #za pomoca funckji sorted()
list_to_sort.sort(key=lambda x: (x[1], x[2])); #za pomocą metody sort();
print(list_to_sort)
print(sorted_list)
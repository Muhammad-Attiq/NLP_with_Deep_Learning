list1 = [int(x) for x in input("Enter first list: ").split()]
list2 = [int(x) for x in input("Enter second list: ").split()]

merged_list = list1 + list2
merged_list.sort()

print("Merged and sorted list:", merged_list)

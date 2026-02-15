list1 = [int(x) for x in input("Enter first list: ").split()]
list2 = [int(x) for x in input("Enter second list: ").split()]

merged_list = list1 + list2
merged_list.sort()

smallest = merged_list[0]
largest = merged_list[-1]

print("Merged and sorted list:", merged_list)
print("Smallest element:", smallest)
print("Largest element:", largest)

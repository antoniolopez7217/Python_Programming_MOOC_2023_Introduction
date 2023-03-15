# Please write a function named list_sum which takes two lists of integers as arguments. 
# The function returns a new list which contains the sums of the items at each index in the two original lists. 
# You may assume both lists have the same number of items.

# An example of the function at work:

# a = [1, 2, 3]
# b = [7, 8, 9]
# print(list_sum(a, b)) # [8, 10, 12]

def list_sum(list1, list2):
	sum_list = []
	for i in range(len(list1)):
		sum_list.append(list1[i] + list2[i])
	return sum_list

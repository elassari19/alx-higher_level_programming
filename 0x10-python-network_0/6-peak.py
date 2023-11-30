#!/usr/bin/python3
'''
should write a function that finds a peak in a list of unsorted integers
'''


def find_peak(list_of_integers):
	'''
	should finds a peak in a list
	'''
	list_integers = list_of_integers
	if list_of_integers == []:
			return None
	length = len(list_of_integers)

	start, end = 0, length - 1
	while start < end:
			mid = start + (end - start) // 2
			if list_of_integers[mid] > list_of_integers[mid - 1] and list_of_integers[mid] > list_of_integers[mid + 1]:
					return list_integers[mid]
			if list_of_integers[mid - 1] > list_of_integers[mid + 1]:
					end = mid
			else:
					start = mid + 1
	return list_integers[start]

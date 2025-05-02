# 6-1
strings = ['The', 'quick', 'brown']
assert ([len(elm) for elm in strings] == [3, 5, 5])

str1 = '123,45,-3'
assert ([int(elm) for elm in str1.split(',')] == [123, 45, -3])

def var(lst):
	sum = 0
	for elm in lst:
		sum += elm
	mean = sum / len(lst)
	sum_sq = 0
	for elm in lst:
		sum_sq += (elm - mean) ** 2
	va = sum_sq / (len(lst))
	return va
assert (var([3,4,1,2]) == 1.25)

def sum_lists(list1):
	return sum([sum(lst) for lst in list1])

assert (sum_lists([[20, 5], [6, 16, 14, 5], [16, 8, 16, 17, 14], [1], [5, 3, 5, 7]]) == 158)

def sum_matrix(list1, list2):
	return [[list1[i][j] + list2[i][j] for j in range(3)] for i in range(3)]

assert (sum_matrix([[1,5,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]])==[[2, 9, 10], [6, 10, 14], [10, 14, 18]])

# 6-2
def max_value_key(d):
	return max(d, key=lambda k: d[k])

assert (max_value_key({3:10, 5:2, 9:1}) == 3)

def max_abs(ln):
	return max(map(abs, ln))

assert (max_abs([3,-8,1,0,7,-5]) == 8)


def number_of_big_numbers(ln, n):
	return len(list(filter(lambda x: x > n, ln)))

assert (number_of_big_numbers([10, 0, 7, 1, 5, 2, 9], 5) == 3)

def number_of_long_lines(file, n):
	with open(file, 'r', encoding='utf-8') as f:
		return sum(map(lambda x: 1), filter(lambda x: len(x) > n, f))
	
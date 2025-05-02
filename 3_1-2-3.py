# 3-1
def reverse_lookup(list1):
	return_dict = {}
	i = 0
	for val in list1:
		return_dict[val] = i
		i += 1
	return return_dict

assert (reverse_lookup(['apple', 'pen', 'orange']) == {'apple': 0, 'orange': 2, 'pen': 1})

# dic1.get(key)とdic1[key]でvalueを取得する違いは、valueがない時Noneになるかエラーになるかの違い
def handle_collision(dic1, str1):
	if (dic1.get(len(str1))) is None:
		ls = [str1]
	else:
		ls = dic1.get(len(str1)) # dic1[len(str1)]でもいい。
		ls.append(str1)
	dic1[len(str1)] = ls


dic1_orig = {3: ['ham', 'egg'], 6: ['coffee', 'brandy'], 9: ['port wine'], 15: ['curried chicken']}
dic1_result = {3: ['ham', 'egg', 'tea'], 6: ['coffee', 'brandy'], 9: ['port wine'], 15: ['curried chicken']}
handle_collision(dic1_orig, 'tea')
assert (dic1_orig == dic1_result)

# 3-2
def reverse_lookup2(dic1):
	dic2 = {}
	for key, val in dic1.items():
		dic2[val] = key
	return dic2

assert (reverse_lookup2({'apple': 3, 'pen': 5, 'orange': 7}) == {3: 'apple', 5: 'pen', 7: 'orange'})

def sum_n(x, y):
	sum = 0
	for val in range(x, y+1):
		sum += val
	return sum

assert (sum_n(1, 3) == 6)

def construct_list(int_size):
	return [x for x in range(int_size)]

assert (construct_list(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

def sum_lists(list1):
	sum = 0
	for elm in list1:
		for idx in range(len(elm)):
			sum += elm[idx]
	return sum

assert (sum_lists([[20, 5], [6, 16, 14, 5], [16, 8, 16, 17, 14], [1], [5, 3, 5, 7]])  == 158)

def simple_match(str1, str2):
	flag = 0
	for i in range(len(str1) - len(str2) + 1):
		cnt = 0
		for j in range(len(str2)):
			if (str1[i + j] != str2[j]):
				break
			cnt += 1
		if (cnt == len(str2)):
			return i

	return -1

assert (simple_match('location', 'cat') == 2)
assert (simple_match('soccer', 'cat') == -1)
assert (simple_match('category', 'cat') == 0)
assert (simple_match('carpet', 'cat') == -1)

from time import sleep

i = 0
while i < 10:
	i += 1
	# print('Yeah!')
	sleep(0.01)
assert i == 10

import re
"""
正規表現について
[^...]	中のいずれか以外の1文字    e.g.) [^0-9] → 数字以外
+	直前の文字の1回以上の繰り返し   e.g.) a+ → a, aaa
"""
def collect_engwords(str_engsentence):
	return_list = []
	split_text = re.split(r'[^a-zA-Z]+', str_engsentence)
	for val in split_text:
		if (len(val) < 3):
			continue
		return_list.append(val)
	return return_list

assert (collect_engwords('Unfortunately no, it requires something with a little more kick, plutonium.') == ['Unfortunately', 'requires',
'something', 'with', 'little', 'more', 'kick', 'plutonium'])

def swap_lists(ln1, ln2):
	for i, val in enumerate(ln1[1::2]):
		tmp = ln2[2*i+1]
		ln2[2*i+1] = val
		ln1[2*i+1] = tmp

	return (ln1, ln2)

assert (swap_lists([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']) == ([1, 'b', 3, 'd', 5], ['a', 2, 'c', 4, 'e']))

def count_capitalletters(str1):
	cnt = 0
	for val in str1:
		if ((val >= 'A' and val <= 'Z')):
			cnt += 1
	return cnt

assert (count_capitalletters('Que Será, Será') == 3)

def identify_codons(str_augc):
	result = []
	i = 0
	while i < len(str_augc):
		str = str_augc[i:i+3]
		result.append(str)
		i += 3
	return result

assert (identify_codons('CCCCCGGCACCT') == ['CCC', 'CCG', 'GCA', 'CCT'])

def add_commas(int1):
	str_int1 = str(int1)[::-1]
	result = ''
	for i in range(0, len(str_int1), 3):
		result += str_int1[i:i+3] + ','
	result = result.rstrip(',')
	return result[::-1]


assert (add_commas(14980) == '14,980')
assert (add_commas(3980) == '3,980')
assert (add_commas(298) == '298')
assert (add_commas(1000000) == '1,000,000')

def sum_strings(list1):
	s = ''
	if len(list1) == 1:
		return list1[0]
	elif len(list1) == 2:
		s = list1[0] + ', ' + list1[1]
	else:
		i = 0
		while i < len(list1):
			if (isinstance(list1[i], int)):
				s += str(list1[i])
			else:
				s += list1[i]

			if i < len(list1) - 2:
				s += ', '
			elif i == len(list1) - 2:
				s += ' and '
			else:
				pass
			i += 1
	return s

assert (sum_strings(['a', 'b', 'c', 'd']) == 'a, b, c and d')
assert (sum_strings(['a']) == 'a')
assert (sum_strings([1, 2, 3]) == '1, 2 and 3')

def handle_collision2(dic1, str1):
	if (dic1.get(len(str1)) == None):
		dic1[len(str1)] = str1
	else:
		for i in range(len(str1),11):
			if (dic1.get(i) == None):
				dic1[i] = str1
				return
		for i in range(1, len(str1)):
			if (dic1.get(i) == None):
				dic1[i] = str1
				return

dic1_orig = {6: 'Styles', 4: 'Link', 7: 'Ackroyd'}
handle_collision2(dic1_orig, 'Big Four')
assert (dic1_orig == {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four'})
dic1_orig = {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House'}
handle_collision2(dic1_orig, 'Edgware')
assert (dic1_orig == {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House', 1: 'Edgware'})
dic1_orig = {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House', 1: 'Edgware', 2: 'Orient', 3: 'Three Act', 5: 'Clouds'}
handle_collision2(dic1_orig, 'ABC')
assert (dic1_orig == {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House', 1: 'Edgware', 2: 'Orient', 3: 'Three Act', 5: 'Clouds'})


def handle_collision3(list1):
	result = {}
	for list2 in list1:
		if (result.get(list2[0]) == None):
			result[list2[0]] = list2[1]
	return result

assert (handle_collision3([[3, 'Richard III'], [1, 'Othello'], [2, 'Tempest'], [3, 'King John'], [4, 'Midsummer'], [1, 'Lear']]) == {1: 'Othello', 2: 'Tempest', 3: 'Richard III', 4: 'Midsummer'})

# 3-3
# なし

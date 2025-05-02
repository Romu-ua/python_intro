# 3-1
def remove_punctuations(str_engsentences):
	str_engsentences = str_engsentences.replace('.', '')
	str_engsentences = str_engsentences.replace(',', '')
	str_engsentences = str_engsentences.replace(':', '')
	str_engsentences = str_engsentences.replace(';', '')
	str_engsentences = str_engsentences.replace('!', '')
	str_engsentences = str_engsentences.replace('?', '')
	return str_engsentences

assert remove_punctuations('Quiet, uh, donations, you want me to make a donation to the coast guard youth auxiliary?') == 'Quiet uh donations you want me to make a donation to the coast guard youth auxiliary'

def atgc_bppair(str_atgc):
	str_pair = str_atgc.replace('A', 't')
	str_pair = str_pair.replace('T', 'a')
	str_pair = str_pair.replace('G', 'c')
	str_pair = str_pair.replace('C', 'g')
	str_pair = str_pair.upper()
	return str_pair
assert atgc_bppair('AAGCCCCATGGTAA') == 'TTCGGGGTACCATT'

def swap_colon(str1):
	idx = str1.find(':')
	fstr = str1[:idx]
	sstr = str1[idx+1:]
	return sstr + ':' + fstr
assert swap_colon('hello:world') == 'world:hello'

def atgc_count(str_atgc, str_bpname):
	return str_atgc.count(str_bpname)
assert atgc_count('AAGCCCCATGGTAA', 'G') == 3

def check_lower(str_engsentences):
	if str_engsentences == str_engsentences.lower():
		return True
	else:
		return False
assert (check_lower('down down down') == True)
assert (check_lower('There were doors all round the hall, but they were all locked') == False)

def remove_clause(str_engsentences):
	idx = str_engsentences.find(',')
	sub_str = str_engsentences[idx+2:]
	sub_str = sub_str.capitalize()
	return sub_str
assert (remove_clause("It's being seen, but you aren't observing.")  == "But you aren't observing.")

# 2-2
def remove_evenindex(ln):
	even_list = ln[1::2]
	return even_list

assert (remove_evenindex(['a', 'b', 'c', 'd', 'e', 'f', 'g']) == ['b', 'd', 'f'])
assert (remove_evenindex([1, 2, 3, 4, 5]) == [2, 4])

def change_domain(email, domain):
	split_email = email.split('@')
	split_email[1] = '@' +  domain
	return ''.join(split_email)

assert (change_domain('spam@utokyo-ipp.org', 'ipp.u-tokyo.ac.jp') == 'spam@ipp.u-tokyo.ac.jp')

def reverse_totuple(ln):
	reverse_ln = ln[::-1]
	return tuple(reverse_ln)

assert (reverse_totuple([1, 2, 3, 4, 5]) == (5, 4, 3, 2, 1))

def sum_list(ln):
	sum = 0
	for val in ln:
		sum += val
	return sum

assert (sum_list([10, 20, 30]) == 60)
assert (sum_list([-1, 2, -3, 4, -5]) == -3)

def atgc_countlist(str_atgc):
	a, t, g, c = 0, 0, 0, 0
	for val in str_atgc:
		if (val == 'A'):
			a += 1
		elif (val == 'T'):
			t += 1
		elif (val == 'G'):
			g += 1
		elif (val == 'C'):
			c += 1
	return (sorted(([a, 'A'], [t, 'T'], [g, 'G'], [c, 'C'])))

assert (sorted(atgc_countlist('AAGCCCCATGGTAA')) == sorted([[5, 'A'], [2, 'T'], [3, 'G'], [4, 'C']]))

# 2-3
def exception3(x, y, z):
	if x == y:
		return z
	elif x == z:
		return y
	elif y == z:
		return x

assert (exception3(1,2,2) == 1)
assert (exception3(4,2,4) == 2)
assert (exception3(9,3,9) == 3)

def exception9(a):
	a.sort()
	if (a[0] != a[1]):
		return a[0]
	else:
		return a[-1]

assert (exception9([1,2,2,2,2,2,2,2,2]) == 1)
assert (exception9([4,4,4,4,4,2,4,4,4]) == 2)
assert (exception9([9,9,9,9,9,9,9,9,3]) == 3)

x = -1
if 2 <= x and x < 3:
	print('x is larger than or equal to 2, and less than 3')
elif 1 <= x and x < 2:
	print('x is larger than or equal to 1, and less than 2')
elif x < 1:
	print('x is less than 1')
else:
	print('x is larger or equal to 3')

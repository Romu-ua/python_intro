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
print(remove_clause("It's being seen, but you aren't observing.")  == "But you aren't observing.")
import math
# 1-1
# print((math.sqrt(5) + 1) / 2)

# 1-2
def ft_to_cm(f, i):
	return (f * 12 + i) / 12 * 30.48

assert round(ft_to_cm(5, 2) - 157.48, 6) == 0
assert round(ft_to_cm(6, 5) - 195.58, 6) == 0

def quadratic(a, b, c, x):
	return (a * x * x + b * x + c)

assert quadratic(1, 2, 1, 3) == 16
assert quadratic(1, -5, -2, 7) == 12

def qe_disc(a, b, c):
	return b * b - 4 * a * c

def qe_solutions1(a, b, c):
	return (-b - math.sqrt(qe_disc(a, b, c))) / (2 * a)

def qe_solutions2(a, b, c):
	return (-b + math.sqrt(qe_disc(a, b, c))) / (2 * a)

assert qe_disc(1, -2, 1) == 0
assert qe_disc(1, -5, 6) == 1
assert round(qe_solutions1(1, -2, 1) - 1, 6) == 0
assert round(qe_solutions2(1, -2, 1) - 1, 6) == 0
assert round(qe_solutions1(1, -5, 6) - 2, 6) == 0
assert round(qe_solutions2(1, -5, 6) - 3, 6) == 0

# 1-3
def absolute(x):
	if (x >= 0):
		return x
	else:
		return -x
assert absolute(5) == 5
assert absolute(-5) == 5
assert absolute(0) == 0

def sign(x):
	if (x > 0):
		return 1
	elif (x < 0):
		return -1
	else:
		return 0
	
assert sign(5) == 1
assert sign(-5) == -1
assert sign(0) == 0
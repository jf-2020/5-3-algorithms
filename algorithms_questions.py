# algorithms_questions.py - this prgm will solve the 3 problems 
#							from 5/3's algorithms' questions
#
# jf - 5/3

def find_factors(n):
	''' solve problem 1 '''
	factors = list()
	for factor in range(1, n+1):
		if n % factor == 0:
			factors.append(factor)
	return factors

def test_find_factors():
	''' unit test for find_factors() function '''
	test1 = [10, 11, 111, 321421, 412146]
	for test in test1:
		print("Testing {} on find_factors({})".format(test, test))
		print("Answer: {}".format(find_factors(test)))

def same_frequency(num1, num2):
	''' solve problem 2 '''
	l1, l2 = list(str(num1)), list(str(num2))
	# now sort the list of chars
	l1.sort()
	l2.sort()
	# recombine them into strings
	s1, s2 = ''.join(l1), ''.join(l2)
	# iterate over both strings and see if they're
	# corresponding chars are ==
	for index, char in enumerate(s1):
		# check if they're not equal
		if char != s2[index]:
			# if so, then the freqs aren't ==
			return False
	return True

def test_same_frequency():
	''' unit test for same_frequency() function '''
	test2 = [(551122, 221515), (321142, 3212215), (1212, 2211)]
	for test in test2:
		print("Testing ({}, {}) on same_frequency({}, {})".format(test[0], test[1], test[0], test[1]))
		print("Answer: {}".format(same_frequency(test[0], test[1])))

def three_odd_numbers(nums):
	''' solves problem 2 '''
	# if the list doesn't have at least 3 nums
	if len(nums) < 3:
		# then wrong
		return False
	# now, iterate over list, not including last 2 items
	for index in range(len(nums)-3):
		# see if the sum is not even
		if (nums[index] + nums[index+1] + nums[index+2]) % 2 != 0:
			# then it's right
			return True
	# otherwise it's wrong
	return False

def test_three_odd_numbers():
	''' unit test for three_odd_numbers() function '''
	test3 = [
				[1, 2, 3, 4, 5],
				[0, -2, 4, 1, 9, 12, 4, 1, 0],
				[5, 2, 1],
				[1, 2, 3, 3, 2]
			]
	for test in test3:
		# print("Testing {} on three_odd_numbers({})".format(test))
		# print("Answer: {}".format(three_odd_numbers(test)))
		print(three_odd_numbers(test))

def main():
	### testing question 1 ###
	test_find_factors()
	print()

	### testing question 2 ###
	test_same_frequency()
	print()

	### testing question 3 ###
	test_three_odd_numbers()

if __name__ == "__main__":
	main()
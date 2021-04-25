import re
import time

t = time.time()

with open("data.txt") as f:
	data = f.read().splitlines()
	
def apply_op(data):
	nums = [int(i) for i in (re.findall('\d+', data))]
	ops  = [i for i in data if i == "+" or i =="*"]
	while len(nums) > 1:
		a,b  = nums[0:2]
		op = ops[0]
		if op == "+":
			c = a+b
		else:
			c = a*b
		del ops[0]
		del nums[0:2]
		nums.insert(0,c)
	return nums[0]

# "1 + 2 * 3 + 4 * 5 + 6"
# [1,2,3,4,5,6]
# [+,*,+,*,+]

# + = *
# * = +

# def operator(+,a,b):
# 	return a*b


def solv(data):
	while "(" in data:
		sub = parser(data)
		num = apply_op(sub)
		data = data.replace(sub,str(num))

	return apply_op(data)

def parser(data):
	sol = None
	sag = None
	for indx,val in enumerate(data):
		if val == "(":
			sol = indx
		elif val == ")":
			sag = indx
		if sol != None and sag != None:
			return data[sol:sag+1]


ans1 = 0
for dat in data:
	ans1 += solv(dat)

print(ans1)

print(time.time()-t)
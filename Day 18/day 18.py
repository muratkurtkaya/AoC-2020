import re
import time
import numpy as np

t = time.time()

with open("data.txt") as f:
	data = f.read().splitlines()
	
def apply_op(data):
	nums = [int(i) for i in (re.findall('\d+', data))]
	ops  = [i for i in data if i == "+" or i =="*"]
	while ops != []:
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

def apply_op_part2(data):
	nums = [int(i) for i in (re.findall('\d+', data))]
	ops  = [i for i in data if i == "+" or i =="*"]
	while "+" in ops:
		indx = ops.index("+")
		a,b  = nums[indx:indx+2]
		c = a+b
		del ops[indx]
		del nums[indx:indx+2]
		nums.insert(indx,c)
	return np.prod(np.array(nums),dtype=np.int64) #int64, otherwise it is truncated


def solve(data,part=1):
	while "(" in data:
		sub = parser(data)
		if part == 1:
			num = apply_op(sub)
		else:
			num = apply_op_part2(sub)
		data = data.replace(sub,str(num))
	return apply_op(data) if part==1 else apply_op_part2(data)



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
ans2 = 0
for dat in data:
	ans1 += solve(dat,part=1)
	ans2 += solve(dat,part=2)

print("ans1:",ans1)
print("ans2:",ans2)

print(time.time()-t)


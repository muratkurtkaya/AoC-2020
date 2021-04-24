from collections import defaultdict

nums = defaultdict(list)
puzzle = [9,19,1,6,0,5,4]

for i,k in enumerate(puzzle): #creating dict
	nums[k].append(i+1)

last = puzzle[-1]
for turn in range(len(puzzle)+1,30000000+1):
	#if last number spoken first time, then next number is
	if last in nums:
		if len(nums[last]) <= 1:
			last = 0
			nums[last].append(turn)
		else:
			last = nums[last][-1] - nums[last][-2]
			nums[last].append(turn)
	else:
		nums[last].append(turn)

for k,v in nums.items():
	if 30000000 in v:
		ans = k

print(ans)


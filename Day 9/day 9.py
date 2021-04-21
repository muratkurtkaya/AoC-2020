import numpy as np 

with open("puzzle.txt") as f:
	puzzle = [int(x) for x in f]



def solv1(data):
	for indx,num in enumerate(data):
		if indx < 25:
			continue

		flag = False
		for i in range(25):
			for j in range(i,25):
				if j!=i and data[indx-i-1]+data[indx-j-1] == num :
					flag = True
		
		if flag == False:
			return data[indx]
			
ans1 = solv1(puzzle)
print("ans1:",ans1)

def solv2(puzzle,ans):
	for i in range(len(puzzle)):
		for j in range(i,len(puzzle)):
			tmp_data = puzzle[i:j].copy()
			if np.sum(tmp_data) == ans:
				# print("ans2:",tmp_data)
				return tmp_data

ansData = solv2(puzzle, ans1)
print("ans2:",np.min(ansData)+np.max(ansData))
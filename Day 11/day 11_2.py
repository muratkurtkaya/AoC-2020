import numpy as np
data = np.loadtxt("data.txt",dtype= object)

arr = np.zeros((len(data),len(data[0])))


for i in range(len(data)):
	for j in range(len(data[0])):
		arr[i][j] = ord(data[i][j])

def check(data,i,j):
	cnt = 0
	a = [(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,-1),(1,0),(1,1)]
	for iii,jjj in a:
		ii = i+iii
		jj = j+jjj
		if ii<0 or jj<0 or ii>=len(data) or jj >=len(data[0]):
			continue

		while data[ii][jj] == ord(".") and not (ii+iii<0 or jj+jjj<0 or ii+iii>=len(data) or jj+jjj>=len(data[0])):
			ii += iii
			jj += jjj
		
		if data[ii][jj] == ord("#"):
			cnt += 1

	return cnt


def change(data):
	tmp = data.copy()
	x = True
	for i,sub in enumerate(data):
		for j,it in enumerate(sub):
			cnt = check(data, i, j)
			# print(cnt)
			if data[i][j] == ord("#") and cnt>=5:
				tmp[i][j] = ord("L")
				x = False
			elif data[i][j] == ord("L") and cnt==0:
				tmp[i][j] = ord("#")
				x = False
	 #return true if there is no change

	return tmp,x

def solv1(arr):
	k = False
	while not k:
		arr,k = change(arr)
	print("empy seats:",np.sum(arr==ord("#")))

solv1(arr)

import numpy as np

with open("data.txt") as f:
	data = f.read().splitlines()

print("Lenght of list",len(data))



def solv1(data):
	lineLogs = [0] #logs of visited lines
	cnt = 0
	acc = 0
	for _ in range(len(data)):
		# print(acc)
		try:
			word,num = data[cnt].split()
		except:
			print(acc) #for part2, if cnt out of index then program fixed
		num = int(num)
		if word == "acc":
			acc += int(num)
			cnt += 1
		elif word == "nop":
			cnt += 1
		elif word =="jmp":
			cnt += int(num) 

		if cnt not in lineLogs:
			lineLogs.append(cnt)
		else:
			return acc,cnt
	return acc
ans1,_ = solv1(data)
print(ans1)

#part2
for i in range(len(data)):
	tmpData = data.copy()
	# print(data[i])
	if data[i].split()[0] == "nop":
		tmpData[i] = "jmp" + tmpData[i][3:]
	elif data[i].split()[0] == "jmp":
		tmpData[i] = "nop" + tmpData[i][3:]
	solv1(tmpData)
	# print(solv1(tmpData),"i:",i)





with open("yes.txt") as f:
	data = f.read().split("\n\n")

def solv1(inData):
	y = []
	count = 0
	for x in inData:
		for i in x:
			if i.isalpha() and i not in y:
				y.append(i)
		count += len(y)
		y = []
	return count

def solv2(inData):
	count = 0
	for s in inData:
		x = s.split("\n") #splits group members
		intersection = set(x[0]) 
		for y in x[1:]:
			intersection.intersection_update(y)
		count += len(intersection)
	return count


ans1 = solv1(data)
ans2 = solv2(data)
print(ans1,ans2)
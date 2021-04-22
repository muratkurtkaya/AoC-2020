with open("data.txt") as f:
	data = f.read().splitlines()

busses = []

for i,dat in enumerate(data[1].split(",")):
	if dat != "x":
		busses.append((int(dat),i))
busses.sort(reverse=True)

print(busses)

#Brute force?



with open("data.txt") as f:
	data = f.read().splitlines()

timestamp = int(data[0])
buss = [int(i) for i in data[1].split(",") if i!="x"]

flag = False
tmp = timestamp
while not flag:
	for bus in buss:
		if tmp%bus == 0:
			print("ans:",(tmp-timestamp)*bus)
			flag = True
	tmp += 1







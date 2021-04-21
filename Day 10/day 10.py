data = [int(x) for x in open("data.txt")] #more elegant than using "with"

data.append(0) #first jolt=0
data.sort()

ones = 0
three = 1
for i in range(len(data)-1):
	diff = data[i+1] - data[i]
	# print(data[i+1])
	if diff == 1:
		ones += 1
	elif diff == 3:
		three +=1

print(ones,three,"ans:",ones*three)


counter = [1] * len(data)

#super clever solution by someone(not me.)
for i in range(1, len(data)):
    counter[i] = counter[i - 1]
    if i > 1 and data[i] - data[i - 2] <= 3:
        counter[i] += counter[i - 2]
    if i > 2 and data[i] - data[i - 3] <= 3:
        counter[i] += counter[i - 3]

ans2 = counter[-1]
print(ans2)
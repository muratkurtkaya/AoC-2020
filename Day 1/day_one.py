
def part1(data):
    for i in data:
        if(2020-i) in data:
            return i * (2020-i)

def part2(data):
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if(2020-data[i]-data[j]) in data:
                return data[i]*data[j]*(2020-data[i]-data[j])

values = []
f = open("values.txt","r")
for line in f.readlines():
    values.append(int(line))

ans1 = part1(values)
ans2 = part2(values)

print(ans1,ans2)

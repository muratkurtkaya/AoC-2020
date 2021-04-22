with open("data.txt") as f:
	data = f.read().splitlines()

# print(data)

def changer(text,dire):
	direcs = ["W","N","E","S"]
	pos = direcs.index(dire)
	deg = int(int(text[1:])/90)
	if text[0] == "R":
		pos += deg
	else:
		pos -= deg
	pos %= 4
	return direcs[pos]

def move(pos,text,dire):
	direcs = ["W","N","E","S"]
	if text[0] == "F":
		indx = direcs.index(dire)
		pos[indx] += int(text[1:])
	else:
		indx = direcs.index(text[0])
		pos[indx] += int(text[1:])
	return pos

pos = [0,0,0,0] #WNES

dire = "E"
for dat in data:
	if dat[0] == "R" or dat[0] == "L":
		dire = changer(dat, dire)
	else:
		pos = move(pos, dat, dire)

print(abs(pos[0]-pos[2])+abs(pos[1]-pos[3]))
# print(changer("L270","N"))
with open("data.txt") as f:
	data = f.read().splitlines()

def changer(text,waypoint):
	direcs = ["W","N","E","S"]
	tmp = []
	for dire in waypoint:
		pos = direcs.index(dire[0])
		deg = int(int(text[1:])/90)
		if text[0] == "R":
			pos += deg
		else:
			pos -= deg
		pos %= 4
		tmp.append(direcs[pos]+str(dire[1:]))
	return tmp

def move(pos,text,waypoint):
	direcs = ["W","N","E","S"]
	for way in waypoint:
		indx = direcs.index(way[0])
		pos[indx] = pos[indx] + int(text[1:])*int(way[1:])
	return pos

def increment(text,wy):
	direcs = []
	for w in wy:
		direcs.append(w[0])
	indx = direcs.index(text[0])
	wy[indx] = wy[indx][0] + str(int(wy[indx][1:])+int(text[1:]))
	return wy

waypoint = ["W0","N1","E10","S0"]
pos = [0,0,0,0] #WNES

for dat in data:
	if dat[0] == "R" or dat[0] == "L":
		waypoint = changer(dat, waypoint)
	elif dat[0] == "F":
		pos = move(pos, dat, waypoint)
	else:
		waypoint = increment(dat, waypoint)

print("distance:", abs(pos[0]-pos[2])+abs(pos[1]-pos[3]))

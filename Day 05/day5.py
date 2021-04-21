with open("seats.txt") as f:
	seats = f.read().splitlines()

# F->0-63 lower half, B->64-127 upper half
# L-> lower, R-> upper

def rowCalc(seatId):
	#basically F=0, B=1 then convert binary to decimal.
	row = 0
	for indx,s in enumerate(seatId[:7]):
		if s == "B":
			row += 2**(6-indx)
	return row

def colCalc(seatId):
	col = 0
	for indx,s in enumerate(seatId[-3:]):
		if s == "R":
			col += 2**(2-indx)
	return col

seat_all = []
ans1 = -1
for seat in seats:
	id = rowCalc(seat) * 8 + colCalc(seat)
	if id > ans1:
		ans1 = id
	seat_all.append(id)	

seat_all.sort() 

for i in range(seat_all[0],seat_all[-1]):
	if i not in seat_all:
		ans2 = i

print(ans1,ans2)
with open("data.txt") as f:
	data = f.read().splitlines()

def apply_mask(mask,val):
	num = ""
	for indx,tmp in enumerate(mask):
		if tmp == "X":
			num += val[indx]
		else:
			num += tmp
	return int(num,2)


mask = None
cur_address = None
memory_log = {}

for dat in data:
	typ,val = dat.split(" = ")
	# print(typ)
	if typ == "mask":
		mask = val #update mask
	else:
		bin_num = bin(int(val))[2:].zfill(36) #36 bits
		updated_val = apply_mask(mask, bin_num)
		memory_log[typ[4:-1]] = updated_val

ans = 0
for k,v in memory_log.items():
	ans += v

print(ans)


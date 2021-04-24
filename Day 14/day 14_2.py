import itertools

with open("data.txt") as f:
	data = f.read().splitlines()

def apply_mask(mask,val):
	num = ""
	for indx,tmp in enumerate(mask):
		if tmp == "X":
			num += "X"
		elif tmp == "0":
			num += val[indx]
		else:
			num += "1"
	return num

def address_combination(mem_address):
	addresses = []
	all_values = [0]
	val = 0
	for indx,item in enumerate(mem_address):
		if item == "1":
			val += 2**(35-indx)
		elif item == "X":
			all_values.append(2**(35-indx))

	for L in range(1,len(all_values)+1):
		for subset in itertools.combinations(all_values, L):
			tmp_val = val + sum(subset)
			if tmp_val not in addresses:
				addresses.append(tmp_val)
	return addresses

mask = None
cur_address = None
memory_log = {}

for dat in data:
	typ,val = dat.split(" = ")
	# print(typ)
	if typ == "mask":
		mask = val #update mask
	else:
		bin_mem = bin(int(typ[4:-1]))[2:].zfill(36) #36 bits
		updated_mem = apply_mask(mask, bin_mem)
		all_addresses = address_combination(updated_mem)
		for i in all_addresses:
			memory_log[str(i)] = val

# aa = address_combination("000000000000000000000000000000X1101X")
# print(aa)

ans = 0
for k,v in memory_log.items():
	ans += int(v)
print("ans2:",ans)


with open("bags.txt") as f:
	bags = f.read().splitlines()

print("shiny coral bag" in bags[0])



indx = bags[0].index("contain")
print(bags)
def solv1(bags):
	direct_bags = []

	for bag in bags: 
		indx = bag.index("contain")
		if "shiny gold" in bag[indx:]:
			direct_bags.append(bag[:indx].rstrip("bags "))

	for dir_bag in direct_bags:
		for bag in bags:
			indx = bag.index("contain")
			cand_bag = bag[:indx].rstrip("bags ")
			if dir_bag in bag[indx:] and bag[:indx].rstrip("bags ") not in direct_bags:
				direct_bags.append(cand_bag)
	return direct_bags

# def count(bags,bag,sub_count):
	



ans = len(solv1(bags))
print(ans)
#print(direct_bags)

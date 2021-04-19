with open("passport.txt") as f:
    data = f.read()
data = data.split("\n\n")

required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

def byrCheck(x):
	return 2002>=x>=1920

def iyrCheck(x):
	return 2020>=x>=2010

def eyrCheck(x):
	return 2030>=x>=2020

def hgtCheck(x):
	if x[-2:] == "cm":
		return 193>=int(x[:-2])>=150
	elif x[-2:] == "in":
		return 76>=int(x[:-2])>=59
	else:
		return False

def hclCheck(x):
	return x[0] == "#" and len(x) == 7

def eclCheck(x):
	eclCodes = ["amb","blu","brn","gry","grn","hzl","oth"]
	return x in eclCodes

def pidCheck(x):
	return len(x) == 9 



#list of passports with dict
passports = [] 
for item in data:
	passport = {}
	sub_items = item.split()
	for i in sub_items:
		ky,it = i.split(":")
		passport[ky] = it
	passports.append(passport)


ans1 = 0
ans2 = 0
for pw in passports:
	if all(k in pw for k in required_fields): #check all dicts if they contains all keys.
		ans1 += 1
		if byrCheck(int(pw["byr"])):
			if iyrCheck(int(pw["iyr"])):
				if eyrCheck(int(pw["eyr"])):
					if hgtCheck(pw["hgt"]):
						if hclCheck(pw["hcl"]):
							if eclCheck(pw["ecl"]):
								if pidCheck(pw["pid"]):
									ans2 +=1



print(ans1,ans2)



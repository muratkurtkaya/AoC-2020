import re
import numpy as np

with open("data.txt") as f:
	raw_rules,raw_ticket,raw_all_tickets = f.read().split("\n\n")

rules_list = []
rules_flat = []
for rule in raw_rules.split("\n"):
	rule_name,numbers = rule.split(":")
	a,b,c,d = (re.findall('\d+', numbers))
	rules_list.append([(int(a),int(b)),(int(c),int(d))])
	rules_flat.append((int(a),int(b)))
	rules_flat.append((int(c),int(d)))

my_ticket = [int(i) for i in re.findall('\d+',raw_ticket)]

all_tickets = []
for ticket in raw_all_tickets.split(":")[1].split():
	all_tickets.append([int(i) for i in ticket.split(",")] )

def solv1(rules,tickets):
	err = 0
	for ticket in tickets:
		for ticket_val in ticket:
			flag = False
			for rl in rules:
				# print(rule_val)
				if rl[0][0] <= ticket_val <= rl[0][1] or rl[1][0] <= ticket_val <= rl[1][1]:
					flag = True
			if not flag:
				err += ticket_val
	return err

def validate_tickets(rules_flat,tickets):
	valid_tickets = []
	for ticket in tickets:
		cond = all([any(low<=val<=high for (low,high) in rules_flat) for val in ticket])
		if cond:
			valid_tickets.append(ticket)
	return valid_tickets

def check_rule(val,rule):
	if any(low<=val<= high for (low,high) in rule):
		return True
	return False

def solv2(rules,valid_tickets): #rules list #
	rule_table = [[] for i in range(0,20)]
	for k in range(0,20):
		for indx,ticket in enumerate(valid_tickets):
			if all(check_rule(val,rules[k]) for val in ticket):
				rule_table[k].append(indx)
	return rule_table

def find_unique(rule_table):
	unique = [None for i in range(0,20)]
	while None in unique:
		for indx,nums in enumerate(rule_table):
			if len(nums) == 1:
				unique_num = nums[0]
				unique_indx = indx
				for i in range(0,20):
					if unique_num in rule_table[i]:
						rule_table[i].remove(unique_num)
				unique[unique_indx] = unique_num
	return unique


ans1 = solv1(rules_list, all_tickets)
print("ans1:",ans1)

valid_tickets = validate_tickets(rules_flat,all_tickets)

transposed_tickets = np.array(valid_tickets).T

rule_table = solv2(rules_list, transposed_tickets)

	
rule_table = find_unique(rule_table)

ans2 = 1
for i in range(0,6):
	indx = rule_table[i]
	ans2 *= my_ticket[indx]

print("ans2:",ans2)


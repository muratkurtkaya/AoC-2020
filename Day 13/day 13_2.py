with open("data.txt") as f:
	data = f.read().splitlines()

busses = ["x" if i =="x" else int(i) for i in data[1].split(",")] #ignore first line

# chinese division theorem
def solv2(busses):
    mods = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
    vals = list(mods)
    ans = mods[vals[0]]
    inc = vals[0]
    for i in vals[1:]:
        while ans % i != mods[i]:
            ans += inc
        inc *= i
    return ans

print("ans2:",solv2(busses))
with open("passwords.txt", "r") as f:
    strings = f.readlines()


def parser(inStr):
    minV, maxV = inStr.split()[0].split('-')
    car = inStr.split()[1].split(':')[0]
    pw = inStr.split()[2]
    return int(minV), int(maxV), car, pw


def solver1(pws):
    tot = 0
    for strV in pws:
        minV, maxV, car, pw = parser(strV)
        cnt = pw.count(car)
        if maxV >= cnt >= minV:
            tot += 1
    return tot


def solver2(pws):
    tot = 0
    for strV in pws:
        minV, maxV, car, pw = parser(strV)
        if (pw[minV - 1] == car) !=  (pw[maxV - 1] == car): #one of them should contain.
            tot += 1
    return tot


ans1 = solver1(strings)
ans2 = solver2(strings)

print(ans1, ans2)

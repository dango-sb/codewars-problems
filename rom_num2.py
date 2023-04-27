import os
ronu = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "IV": 4, "I": 1}
nuro = {1000: "M", 500:"D",100:"C",50:"L",10:"X",5:"V", 4:"IV", 1:"I"}

def to_roman(val):
    res = []
    vali = str(val)
    n = len(vali) -1
    for j in vali:
            i = int(j)
            if i == 4:
                res.append(nuro[10**n] + nuro[5*10**n])
            elif i == 5:
                res.append(nuro[i*10**n])
            elif i == 9:
                res.append(nuro[10**n] + nuro[10**(n+1)])
            elif i not in [4, 5, 9]:
                if i > 5:
                    res.append(nuro[5 * 10 ** n] + (i-5) * nuro[10**n])
                else:
                    res.append(i * nuro[10 ** n])
            n -= 1

    return ''.join(res)

def from_roman(roman_num):
        res = 0
        l = [ronu[i] for i in roman_num]
        n = len(l)
        for i in range(0, n-1):
            if l[i] >= l[i+1]:
                res += l[i]
            elif l[i] < l[i+1]:
                res -= l[i]

        return res + l[-1]


os.system("clear")
choise = 0
while choise != "s":
    choise = input("\n   input:\n")
    if choise[0] in "1234567890":
        print(to_roman(int(choise)))
    if choise[0] in ronu.keys():
        print(from_roman(choise))


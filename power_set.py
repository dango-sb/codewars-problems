def power(num):

    def power_set(num):
        num_ext = [('', str(i)) for i in num]
        if len(num) == 1:
            return list(num_ext[0])
        else:
            res = [a + b for a in num_ext[0] for b in power_set(num[1:])]
        return res

    res =[list(i) for i in power_set(num) if i != '']
    res2 = []
    for j in res:
        l = []
        for i in j:
            l.append(int(i))
        res2.append(l)
    return res2 + [[]]


    print(power_set([i for i in range(100)]))
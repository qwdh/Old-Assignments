def rdups(ip):
    r = []
    for i in ip:
        if i not in r:
            r.append(i)
    return r

og = [1, 2, 3, 4, 3, 2, 1]
new = rdups(og)
print(new)


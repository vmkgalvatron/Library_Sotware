for i in range(int(input())):
    r = input()
    l = input().split()
    g = list(set(l))
    f = []
    for u in g:
        q = 0
        if l[0] == u:
            q += 1
            j = 2
        else:
            j = 1
        while j < len(l) - 1:
            if l[j] == u and l[j + 1] == u:
                q += q + 1
                j += 2
            elif l[j] == u:
                q += 1
            else:
                j += 1
        f.append(q)
    w = max(f)
    lk = []
    for x in f:
        if x == w:
            lk.append(f.index(x))
    io = []
    for x in lk:
        io.append(int(g[x]))
    print(min(lk))


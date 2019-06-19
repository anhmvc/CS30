def splitList(l):
    if l==[]:
        return [[],[]]
    else:
        first=l[0]
        rest=splitList(l[1:])
        if first%2==0:
            return [[first]+rest[0], rest[1]]
        else:
            return [rest[0], [first]+rest[1]]
def mystery(str1, str2):
    if len(str1) !=len(str2) or len(str1) < 1:
        return ''
    if len(str1) == 1:
        return str1[0] + str2[0]
    return str1[0] + str2[0] + mystery(str1[1:], str2[1:])
    
# mystery("sok", "poy")

def index(l):
    return index_aux(l, 0)

def index_aux(l, i):
    # recursion stuff
    if not l:
        return l
    head = l[0]
    if len(l) == 1:
        return [[head, i]]
print(index("hello"))
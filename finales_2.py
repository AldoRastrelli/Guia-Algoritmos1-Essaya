def merge(L1,L2):

    res = []

    if not L1 or not L2:
        return L1+L2
    
    if L1[0] < L2[0]:

        res.append(L1[0])
        res += (merge(L1[1:],L2))

    else:

        res.append(L2[0])
        res += (merge(L1,L2[1:]))
    
    return res

L1 = [1,3,5,7]
L2 = [2,4,8]

print(merge(L1,L2))
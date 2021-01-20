def permutation(l):
    if len(l)==1:
        return [l]
    llist=[]
    for idx in range(len(l)):
        l_copy=l.copy()
        temp=l_copy.pop(idx)
        for i in permutation(l_copy):
            ll=[temp]
            ll+=i
            llist.append(ll)
            
    return llist

print(permutation([0,1,2]))


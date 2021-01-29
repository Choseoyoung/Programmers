from itertools import combinations
import collections

def solution(orders, course):
    answer = []
    
    for c in course:
        temp=[]
        for order in orders:
            order=''.join(sorted(list(order)))
            for cc in combinations(order,c):
                temp.append(''.join(list(cc)))
        
        most_ordered=collections.Counter(temp).most_common()
        temp=[k for k,v in most_ordered if v>=2 and v==most_ordered[0][1]]
        
        for _ in temp:
            answer.append(_)
    
    return sorted(answer)

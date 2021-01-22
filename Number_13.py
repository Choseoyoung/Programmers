#0 1 2      3        4       5(2*f(2)+1)6            7 8 9
#  1 f(1)*2 f(1)*2+1 f(1)**2 f(1)**2+1 (f(1)*2+1)*2

#n->짝수일때
#return f(n//2)
#n->홀수일때
#return f(n//2)+1
table={1:1}

def solution(n):
    if n in table:
        return table[n]
    else:
        if n%2==0: #n이 짝수일 때
            table[n]=solution(n//2)
            return table[n]
        elif n%2!=0 and n!=1: #n이 홀수일 때
            table[n]=solution(n//2)+1
            return table[n]

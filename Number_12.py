#     1   2
#   1   2   3
# 1   2   3   4
#1 2 3 4 5 6 7 8 #4*2-1 4*2
answer=1
def solution(n,a,b):
    global answer
    if (a-1)//2==(b-1)//2:
        return answer
    else:
        answer+=1
        a,b=(a+1)//2,(b+1)//2
        return solution(n,a,b)

def gcd(big,small):
    if small==0:
        return big
    else:
        return gcd(small,big%small)

def solution(arr):
    a=arr[0]
    for i in range(1,len(arr)):
        b=arr[i]
        a=a*b/gcd(max(a,b),min(a,b))
        
    return a

def solution(arr):
    answer=[0,0]
    
    def check(size,x,y):
        nonlocal answer
        if len(arr)==1:
            answer[arr[0]]+=1
        else:
            temp=arr[y][x]
            
            for dx in range(size):
                for dy in range(size):
                    if arr[y+dy][x+dx]!=arr[y][x]:
                        check(size//2,x,y)
                        check(size//2,x+size//2,y)
                        check(size//2,x,y+size//2)
                        check(size//2,x+size//2,y+size//2)
                        return
            answer[temp]+=1
    check(len(arr),0,0)
    
    return answer

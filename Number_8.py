cnt_0=0
cnt_1=0

def calc_total(arr):
    total=0
    for i in arr:
        total+=sum(i)
    return total

def divide(a):
    arr=[]
    length=len(a)
    global cnt_0
    global cnt_1

    if calc_total(a)==0:
        cnt_0+=1
        a=[0]
        return a
    elif calc_total(a)==len(a)**2:
        cnt_1+=1
        a=[1]
        return a
    if len(a)==1:
        return a

    if len(a)>1:
        #1.
        temp=[]
        for i in range(0,length//2):
            temp.append(a[i][:(length//2):])
        temp=divide(temp)
        arr.append(temp)
        #2.
        temp=[]
        for i in range(0,length//2):
            temp.append(a[i][(length//2):length:])
        temp=divide(temp)
        arr.append(temp)
        #3.
        temp=[]
        for i in range(length//2,length):
            temp.append(a[i][:(length//2):])
        temp=divide(temp)
        arr.append(temp)
        #4.
        temp=[]
        for i in range(length//2,length):
            temp.append(a[i][(length//2):length:])
        temp=divide(temp)
        arr.append(temp)

    a=arr.copy()
    return a

def solution(arr):
    answer=[]
    arr=divide(arr)
    answer.append(cnt_0)
    answer.append(cnt_1)
    return answer

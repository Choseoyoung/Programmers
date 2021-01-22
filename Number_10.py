#[5, 4, 3]   [2, 3, 2]
#[2, 4, 1]   [4, 2, 4]
#[3, 1, 1]   [3, 1, 4]

def solution(arr1, arr2):
    answer = []

    if len(arr1[0])!=len(arr2):
        arr1,arr2=arr2,arr1
    #i행,j열끼리 더하기
    def calc(i,j):
        temp=0
        for idx in range(len(arr1[0])):
            temp+=arr1[i][idx]*arr2[idx][j]
        return temp

    for i in range(len(arr1)):
        ll=[]
        for j in range(len(arr2[0])):
            ll.append(calc(i,j))
        answer.append(ll)

    return answer

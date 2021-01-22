def solution(str1, str2):
    #1.
    str1=str1.upper()
    str2=str2.upper()
    print(str1,str2)
    arr1=[str1[idx:idx+2:] for idx in range(len(str1)-1) if all(s.isalpha()==True for s in str1[idx:idx+2])]
    arr2=[str2[idx:idx+2:] for idx in range(len(str2)-1) if all(s.isalpha()==True for s in str2[idx:idx+2])]
    if len(arr1)<len(arr2):
        arr1,arr2=arr2,arr1
    #2. 교집합 구하기
    temp=list(set([a for a in arr2 if a in arr1]))
    ll=[]
    for a in temp:
        ll+=[a]*min(arr1.count(a),arr2.count(a))
    print(ll)
    #3. 합집합 구하기
    ll2=[a for a in arr1 if a not in temp]+[a for a in arr2 if a not in temp]
    for a in temp:
        ll2+=[a]*max(arr1.count(a),arr2.count(a))
    print(ll2)
    #4.
    if len(ll2)==0:
        answer=1
    else:
        answer=(len(ll)/len(ll2))
    
    return int(answer*65536)

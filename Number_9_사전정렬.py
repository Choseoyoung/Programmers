def solution(nums):
    answer = 0
    
    #1.
    phoneketmon={}
    for i in nums:
        if i not in phoneketmon:
            phoneketmon[i]=1
        else:
            phoneketmon[i]+=1
    #phoneketmon={key:val for key,val in sorted(phoneketmon.items(),key=lambda x: x[1])}
    
    #2.
    if len(phoneketmon)>=len(nums)/2:
        return len(nums)/2
    else:
        return len(phoneketmon)

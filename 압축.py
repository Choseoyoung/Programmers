def solution(msg):
    answer=[]
    alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d={alpha[i]:i+1 for i in range(len(list(alpha)))}
    
    while msg:
        #1.w=현재 입력, temp[0]=다음글자
        w=''
        temp=msg
        
        #2.
        while True:
            if len(temp)==0: break
            w+=temp[0]
            if len(temp)>1: temp=temp[1::] #다음 글자: temp[0]
            else: temp='' #다음글자 없음            
            
            if temp: #다음글자가 있으면
                if w in d and w+temp[0] not in d:
                    answer.append(d[w]) #출력
                    d[w+temp[0]]=len(d)+1 #사전추가
                    msg=temp
                    break
            else:
                answer.append(d[w])
                msg=temp #이후 while문에서 msg=''가 되어 종료
                

    return answer

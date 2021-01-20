import re   

def permu(l):
    if len(l)==1:
        return [l]
    llist=[]
    for idx in range(len(l)):
        l_copy=l.copy()
        temp=l_copy.pop(idx)
        for i in permu(l_copy):
            ll=[temp]
            ll+=i
            llist.append(ll)
    
    return llist

def solution(expression):
    answer = []
    p1=re.compile('\d+')
    p2=re.compile('[-,+,*]')
    m1=p1.findall(expression)
    m2=p2.findall(expression)
    
    def calc(l): #리스트로 우선순위를 전달받으면 값을 계산하여 리턴함
        m_1=m1.copy()
        m_2=m2.copy()
        for i in l:
            while True:
                if i not in m_2:
                    break
                idx=m_2.index(i)
                temp=eval(str(m_1[idx])+str(i)+str(m_1[idx+1]))
                m_1.pop(idx)
                m_1.pop(idx)
                m_2.pop(idx)
                m_1.insert(idx,temp)
        return abs(m_1[0])

    llist=permu(['*','+','-'])
    for i in llist:
        answer.append(calc(i))
    
    return max(answer)

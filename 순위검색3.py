import re

def solution(info, query):
    answer=[0 for _ in range(len(query))]
    
    language={'cpp':set(),'java':set(),'python':set()}
    group={'backend':set(),'frontend':set()}
    career={'junior':set(),'senior':set()}
    soul_food={'chicken':set(),'pizza':set()}
    score={}
    
    #1.
    p=re.compile('(\w+) (\w+) (\w+) (\w+) (\d+)')
    for idx in range(len(info)):
        temp=p.match(info[idx]).groups()
        language[temp[0]].add(idx)
        group[temp[1]].add(idx)
        career[temp[2]].add(idx)
        soul_food[temp[3]].add(idx)
        score[idx]=int(temp[4])
    
    #2.
    p2=re.compile('(\w+|[-]) and (\w+|[-]) and (\w+|[-]) and (\w+|[-]) (\d+)')    
    for idx in range(len(query)):
        temp=p2.match(query[idx]).groups()
        pass_applicants={ _ for _ in range(len(info))}
        if temp[0]!='-': pass_applicants&=language[temp[0]]
        if temp[1]!='-': pass_applicants&=group[temp[1]]
        if temp[2]!='-': pass_applicants&=career[temp[2]]
        if temp[3]!='-': pass_applicants&=soul_food[temp[3]]
        for applicant in pass_applicants:
            if score[applicant]>=int(temp[4]):
                answer[idx]+=1
        
    return answer

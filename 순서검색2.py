def solution(info, query):
    answer=[]
    
    #1.지원자들의 코딩테스트 성적을 기준으로 내림차순 정렬
    info_list=sorted([_.split(' ') for _ in info],key=lambda x:int(x[-1]),reverse=True)
    
    #2.조건을 만족하는 지원자들 수 찾기
    for q in query:
        cnt=0 #조건을 만족하는 지원자 수
        temp=q.replace('and ','').split(' ')
        for applicant in info_list:
            if int(applicant[-1])<int(temp[-1]): break #내림차순
            flag=True
            for idx in range(len(temp[:-1:])):
                if temp[idx]=='-': continue
                if temp[idx]!=applicant[idx]: flag=False; break
            if flag: cnt+=1
        answer.append(cnt)
        
    return answer

def solution(info, query):
    answer=[]
    
    #1.
    info_dict={} #개발언어, 직군, 경력별로 참여자를 모아놓은 사전
    score_dict={} #참여자들의 코딩테스트 성적을 모아놓은 사전
    for idx in range(len(info)):
        score_dict[idx]=int(info[idx].split(' ')[-1])
        temp=info[idx].split(' ')[:-1:]
        for idx2 in range(len(temp)):
            if temp[idx2] in info_dict: info_dict[temp[idx2]].add(idx)
            else: info_dict[temp[idx2]]={idx}
    #2.
    for q in query:
        cnt=0 #해당 조건을 만족하는 참여자 수
        temp=q.replace('and ','').split(' ')
        pass_applicants={_ for _ in range(len(info))}
        for qq in temp[:-1:]:
            if qq=='-': continue
            pass_applicants&=info_dict[qq]
        for applicant in pass_applicants:
            if score_dict[applicant]>=int(temp[-1]): cnt+=1
        answer.append(cnt)
        
    return answer

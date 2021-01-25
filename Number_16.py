def solution(p):
    if p=='': return ''
    
    flag=True #올바른 문자열을 의미
    cnt=0
    for idx in range(len(p)):
        if p[idx]=='(':
            cnt-=1
        elif p[idx]==')':
            cnt+=1
        if cnt>0:
            flag=False
        elif cnt==0:
            u=p[:idx+1:]
            v=p[idx+1::]
            if flag: #올바른 문자열일 경우
                return u+solution(v)
            else: #올바른 문자열이 아닐 경우
                return '('+solution(v)+')'+''.join(list(map(lambda x: ')' if x=='(' else '(' ,u[1:-1:])))

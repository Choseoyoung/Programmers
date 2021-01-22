def solution(s):
    if s=='':
        return 1
    elif all(s[idx]!=s[idx+1] for idx in range(len(s)-1)):
        return 0
    else:
        temp=''
        idx=0
        while idx<len(s)-1:
            if s[idx]==s[idx+1]:
                if idx+2<len(s):
                    temp+=s[idx+2::]
                break
            else: #s[idx]!=s[idx+1]
                temp+=s[idx]
                idx+=1
        return solution(temp)

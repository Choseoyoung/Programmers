import bisect

def solution(info, query):
    answer=[]
    
    root={}
    for applicant in info:
        applicant_info=applicant.split(' ')
        current_root=root
        for information in applicant_info[:-2:]:
            current_root=current_root.setdefault(information,{})
        current_root=current_root.setdefault(applicant_info[-2],[])
        current_root.insert(bisect.bisect_left(current_root,int(applicant_info[-1])),int(applicant_info[-1]))
    
        
    for q in query:
        pass_condition=q.replace('and ','').split(' ')
        cnt=0
        def search(current_root,start,flag=True):
            nonlocal cnt
            idx=start
            for qq in pass_condition[start:-1:]:
                idx+=1
                if qq=='-' and qq not in current_root:
                    for item in current_root.values():
                        search(item,idx,True)
                    flag=False; break
                else:
                    current_root=current_root.get(qq)
                    if current_root==None: flag=False; break
            if flag:
                cnt+=len(current_root)-bisect.bisect_left(current_root,int(pass_condition[-1]))
        search(root,0,True)
        answer.append(cnt)
        
    return answer

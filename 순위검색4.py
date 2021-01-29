def solution(info, query):
    answer=[]
    
    root={}
    for applicant in info:
        current_root=root
        for information in applicant.split(' '):
            current_root=current_root.setdefault(information,{})
        if current_root=={}: current_root['count']=1
        else: current_root['count']+=1
    
    for q in query:
        pass_condition=q.replace('and ','').split(' ')
        cnt=0
        def search(current_root,start,flag=True):
            nonlocal cnt
            idx=start
            for qq in pass_condition[start:-1:]:
                idx+=1
                if qq=='-':
                    for item in current_root.values():
                        search(item,idx,True)
                    flag=False; break
                else:
                    current_root=current_root.get(qq)
                    if current_root==None: flag=False; break
            if flag:
                for key in current_root.keys():
                    if int(key)>=int(pass_condition[-1]): cnt+=current_root[key]['count']
        search(root,0,True)
        answer.append(cnt)
        
    return answer

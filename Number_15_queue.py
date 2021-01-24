from collections import deque

def solution(progresses, speeds):
    answer = []
    
    progresses=deque(progresses)
    speeds=deque(speeds)
    
    while progresses:
        #기능배포 개수 확인
        cnt=0
        while progresses:
            if progresses[0]>=100:
                progresses.popleft()
                speeds.popleft()
                cnt+=1
                continue
            else:
                break
        if cnt!=0:
            answer.append(cnt)
        
        #작업 수행
        for idx in range(len(progresses)):
            cnt=0
            progresses[idx]+=speeds[idx]
    
    return answer

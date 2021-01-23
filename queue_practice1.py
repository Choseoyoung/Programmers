import queue

def solution(bridge_length, weight, truck_weights):
    answer = 0
    onbridge_weight = 0 #다리 위의 트럭들의 무게
    crossed_weight = 0 #다리를 건넌 트럭들의 무게
    weights=sum(truck_weights)
    
    q=queue.Queue(maxsize=bridge_length)
    for _ in range(bridge_length):
        q.put(0)
    
    while crossed_weight<weights:
        answer+=1
        crossed_truck=q.get()
        onbridge_weight-=crossed_truck
        crossed_weight+=crossed_truck
        if len(truck_weights)!=0 and onbridge_weight+truck_weights[0]<=weight: #아직 건널 트럭이 남아 있으면
            onbridge_weight+=truck_weights[0]
            q.put(truck_weights.pop(0))
        else:
            q.put(0)
            
    return answer

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    q_list=[0 for _ in range(bridge_length)]
    truck_crossed=0 #다리를 건넌 트럭들의 무게
    weights=sum(truck_weights) #트럭들의 무게 총합
    
    while truck_crossed<weights:
        answer+=1
        truck_crossed+=q_list.pop(0)
        if len(truck_weights)!=0 and sum(q_list)+truck_weights[0]<=weight:
            q_list.append(truck_weights.pop(0))
        else:
            q_list.append(0)
                   
    return answer

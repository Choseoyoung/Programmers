def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    q_list=[0 for _ in range(bridge_length)]
    truck_bridge=0 #다리 위의 트럭들의 무게
    truck_crossed=0 #다리를 건넌 트럭들의 무게
    weights=sum(truck_weights) #트럭들의 무게 총합
    
    while truck_crossed<weights:
        answer+=1
        truck_out=q_list.pop(0)
        truck_bridge-=truck_out
        truck_crossed+=truck_out
        if len(truck_weights)!=0 and sum(q_list)+truck_weights[0]<=weight:
            truck_in=truck_weights.pop(0)
            truck_bridge-=truck_in
            q_list.append(truck_in)
        else:
            q_list.append(0)
                   
    return answer

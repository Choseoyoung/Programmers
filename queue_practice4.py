def solution(bridge_length, weight, truck_weights):
    answer = 0
    q_list=[0 for _ in range(bridge_length)]
    trucks_onbridge=0 #다리 위의 트럭들의 무게 총합
    trucks_crossed=0 #다리를 건넌 트럭들의 무게 총합
    truck_weights.reverse()
    weights=sum(truck_weights)
    
    while trucks_crossed<weights:
        answer+=1
        truck_out=q_list.pop(0)
        trucks_onbridge-=truck_out #다리 위의 트럭들의 무게 총합
        trucks_crossed+=truck_out
        if len(truck_weights)!=0 and trucks_onbridge+truck_weights[-1]<=weight:
            truck_in=truck_weights.pop(-1)
            q_list.append(truck_in)
            trucks_onbridge+=truck_in
        else:
            q_list.append(0)
        
    return answer

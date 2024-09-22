import heapq as hq
def solution(transitions: list[list[int]], q_initial: int, q_final: int) -> list[int]:

    def convert_to_adj_list(edges):
        adj_list = {}

        for a, b, p in edges:

            if a in adj_list: adj_list[a].append((p, b))
            else: adj_list[a] = [(p, b)]
            if b not in adj_list: adj_list[b] = []

        return adj_list
    
    adj_list = convert_to_adj_list(transitions)

    processed = set()
    predecessor = {state:None for state in adj_list}
    probabilities = {state:0 for state in adj_list}

    probabilities[q_initial] = 1

    if q_final not in probabilities: return 0
    heap = []
    hq.heappush(heap, [-1, q_initial])

    while heap:
        cur_prob, cur_state = hq.heappop(heap)
        cur_prob = -cur_prob

        if cur_state in processed: continue
        processed.add(cur_state)

        for next_transition in adj_list.get(cur_state, []):
            prob, next_state = next_transition

            if cur_prob * prob > probabilities[next_state]:
                probabilities[next_state] = cur_prob * prob
                predecessor[next_state] = cur_state
                hq.heappush(heap, [-probabilities[next_state], next_state])
    
    def construct_path(ancestor):
        path = [ancestor]

        while predecessor[ancestor]!=None:
            path.insert(0, predecessor[ancestor])
            ancestor = predecessor[ancestor]
        return path
        
    return construct_path(q_final)

from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        print(solution(*i), solution(*i)==io_dict[i])
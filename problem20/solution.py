def solution(connections: list[list[int]], treasures: list[int], actions: str, start: int) -> bool: 
    def convert_to_adj_list(edges):
        adj_list = {}

        for a, b, t in edges:
            if a in adj_list: adj_list[a].append((b, t))
            else: adj_list[a] = [(b, t)]

        return adj_list
    
    adj_list = convert_to_adj_list(connections)

    def e_closure(state, stateset):
        stateset.add(state)
        if state not in adj_list: return stateset
        for next, transition in adj_list[state]:
            if next not in stateset and transition=="W":
                stateset.update(e_closure(next, stateset))
        return stateset

    det_adj_list = {}
    nd_to_d_map = {}
    
    stack = []
    processed = set()
    initial = e_closure(start, set())

    nd_to_d_map[frozenset(initial)] = 0
    d_num = 1

    stack.append(initial)
    while stack:
        state = stack.pop()
        if frozenset(state) in processed: continue
        processed.add(frozenset(state))

        for action in range(2):
            newstate = set()
            
            for subnode in state:
                if subnode not in adj_list: continue
                for next, transition in adj_list[subnode]:
                    if transition == action: newstate.add(frozenset(e_closure(next, set())))

            if frozenset(newstate) not in nd_to_d_map:
                nd_to_d_map[frozenset(newstate)] = d_num
                stack.append(newstate)
                d_num+=1
            
            accepting = False
            for possible in newstate:
                if list(possible)[0] in treasures: accepting = True

            if frozenset(state) not in det_adj_list:
                det_adj_list[nd_to_d_map[frozenset(state)]] = [(nd_to_d_map[frozenset(newstate)], action, accepting)]

            else:
                det_adj_list[nd_to_d_map[frozenset(state)]].append((nd_to_d_map[frozenset(newstate)], action, accepting))

    print(det_adj_list, adj_list)

    return True

from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        print(solution(*i))
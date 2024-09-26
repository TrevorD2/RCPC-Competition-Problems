def solution(connections: list[list[int]], treasures: list[int], actions: str, start: int) -> bool: 
    def convert_to_adj_list(edges):
        adj_list = {}

        for a, b, t in edges:
            if a in adj_list: adj_list[a].append((b, t))
            else: adj_list[a] = [(b, t)]

        return adj_list
    
    adj_list = convert_to_adj_list(connections)
    closure_cache = {}

    def e_closure(state):

        if state in closure_cache:
            return closure_cache[state]

        stateset = set([state])

        if state not in adj_list: 
            closure_cache[state] = stateset
            return stateset

        for next, transition in adj_list[state]:
            if next not in stateset and transition=="W":
                stateset = stateset.union(e_closure(next))

        closure_cache[state] = stateset
        return stateset

    cur_state = frozenset(e_closure(start))
    print(cur_state)

    for action in actions:
        next_state = set()

        for substate in cur_state:
            if substate not in adj_list: continue

            for next, transition in adj_list[substate]:
                if transition==int(action):
                    next_state.add(next)
        
        updated = set()
        for state in next_state: 
            updated = updated.union(e_closure(state))

        cur_state = frozenset(updated)
        print(cur_state)

    return any(state in treasures for state in cur_state)

from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        print(solution(*i), solution(*i)==io_dict[i])
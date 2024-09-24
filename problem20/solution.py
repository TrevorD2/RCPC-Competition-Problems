def solution(connections: list[list[int]], treasures: list[int], actions: str, start: int) -> bool: 
    def convert_to_adj_list(edges):
        adj_list = {}

        for a, b, t in edges:
            if a in adj_list: adj_list[a].append((b, t))
            else: adj_list[a] = [(b, t)]

        return adj_list
    
    adj_list = convert_to_adj_list(connections)

    def e_closure(state, stateset=set()):
        stateset.add(state)
        if state not in adj_list: return stateset
        for next, transition in adj_list[state]:
            if next not in stateset and transition=="W":
                stateset.update(e_closure(next, stateset))
        return stateset

    cur_state = frozenset(e_closure(start))
    for action in actions:
        next_state = set()

        for substate in cur_state:
            if substate not in adj_list: continue

            for next, transition in adj_list[substate]:
                if transition==int(action):
                    next_state.update(e_closure(next))
        cur_state = frozenset(next_state)

    for substate in cur_state:
        if substate in treasures: return True

    return False

from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        print(solution(*i), solution(*i)==io_dict[i])
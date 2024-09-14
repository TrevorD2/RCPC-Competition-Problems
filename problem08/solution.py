def solution(connections: list[list[int]], treasures: list[int], actions: str, start: int): 

    def convert_to_adj_list(edges):
        adj_list = {}

        for a, b, t in edges:
            if a in adj_list: adj_list[a].append((b, t))
            else: adj_list[a] = [(b, t)]

        return adj_list
    
    adj_list = convert_to_adj_list(connections)

    pos = start
    for action in actions:
        for door in adj_list[pos]:
            if door[1]==int(action):
                pos = door[0]
                break
        
    return pos in treasures

from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        print(solution(i[0], i[1], i[2], i[3]), solution(i[0], i[1], i[2], i[3])==io_dict[i])
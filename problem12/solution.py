def solution(roads: list[int], n: int) -> bool:
    
    def convert_to_adj_list(edges):
        adj_list = {}

        for a, b in edges:
            if a in adj_list: adj_list[a].append(b)
            else: adj_list[a] = [b]
            if b in adj_list: adj_list[b].append(a)
            else: adj_list[b] = [a]

        return adj_list
    
    adj_list = convert_to_adj_list(roads)

    def backtrack(node, path):
        if len(path) == n: return True
        
        for next in adj_list[node]:
            if next in path: continue
            path.add(next)
            if backtrack(next, path): return True
            path.remove(next)

        return False
    
    for node in adj_list:
        if backtrack(node, set()): return True
    return False

from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        print(solution(*i), solution(*i)==io_dict[i])
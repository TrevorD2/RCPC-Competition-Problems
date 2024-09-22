def solution(connections: list[list[int]], treasures: list[int], actions: str, start: int): 

    def convert_to_adj_list(edges):
        adj_list = {}

        for a, b, t in edges:
            if a in adj_list: adj_list[a].append((b, t))
            else: adj_list[a] = [(b, t)]

        return adj_list
    
    adj_list = convert_to_adj_list(connections)

if __name__ == "__main__": pass
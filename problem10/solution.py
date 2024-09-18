def solution(prerequisites: list[list[int]], course_number: int):
    taken = set()

    def convert_to_adj_list(edges):
        adj_list = {}

        for a, b in edges:
            if a in adj_list: adj_list[a].append(b)
            else: adj_list[a] = [b]

        return adj_list
    
    adj_list = convert_to_adj_list(prerequisites)

    def dfs(course):
        if course not in adj_list: return 0
        total = 0

        for prereq in adj_list[course]:
            if prereq not in taken:
                taken.add(prereq)
                total+=1+dfs(prereq)

        return total
    
    return dfs(course_number)

from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        print(solution(i[0], i[1]), solution(i[0], i[1])==io_dict[i])
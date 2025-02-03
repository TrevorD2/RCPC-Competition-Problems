"""
Problem Notes:
The problem does not specify whether it needs to be shortest path so there are multiple possible answers.
Also, if it does need to be shortest path, there still may be multiple answers; though this scenario is unlikely, you should probably try to prove that there are no duplicates since theres only one "correct" answer.
You should also specify that the sequence will begin with "S", though it could be infered from the example

This solution is just finding any path:
"""
def solution(floors: str) -> str:
    floors = [floor.split("\n") for floor in floors]

    dirdict = {
        (1,0): "D",
        (-1,0): "U",
        (0,-1): "L",
        (0,1): "R"
    }

    def find(char, floor):
        for row in range(len(floor)):
            for col in range(len(floor[row])):
                if floor[row][col] == char: return (row, col)
        return -1
    
    def trace(r, c, path):
        r1, c1 = r, c

        for act in path:
            if act == "U": rl-=1
            elif act == "D": rl+=1
            elif act == "R": c1+=1
            else: c1-=1

        return (r1, c1)

    def solve(start_r, start_c):
        r, c = start_r, start_c
        path = ["S"]
        for floor in floors:
            visited = set()

            def dfs(floor, r, c):
                visited.add((r,c))
                if floor[r][c] == "E": return "E"
                elif floor[r][c] == "T": return "T"

                dir = ((1,0),(0,1),(-1,0),(0,-1))

                for dr, dc in dir:
                    if r+dr>=len(floor) or r+dr<0: continue
                    if c+dc>=len(floor[r+dr]) or c+dc<0: continue
                    if floor[r+dr][c+dc]=="#": continue
                    if (r+dr, c+dc) in visited: continue
                    path = dirdict[(dr,dc)]+dfs(floor, r+dr, c+dc)
                    if path[-1] == "W": continue
                    else: return path

                return "W"

            localpath = dfs(floor, r, c)
            path.append(localpath)
            r, c = trace(r, c, path)
        return "".join(path)


    start_r, start_c = find("S", floors[0])

    return solve(start_r,start_c)

from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        sol = solution(i)
        print(sol, "=", sol==io_dict[i])
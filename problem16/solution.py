from functools import cache
def solution(prices:list[float], springs:list[int], min_force:int, x:float) -> float:
    min_constant = min_force/x
    spring = 0

    @cache
    def dfs(i):
        print("index:", i)
        nonlocal spring
        print(spring)
        if spring >= min_constant: return 0
        if i == len(springs): return float("INF")

        possible = []

        #Add in parallel
        spring+=springs[i]
        print("Price:", prices[i])
        possible.append(prices[i]+dfs(i+1))
        
        #Do not add
        spring = 0
        possible.append(dfs(i+1))
        print(possible)
        return min(possible)
    
    ans = dfs(0)
    return ans if ans!=float("INF") else -1

from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        print(solution(i[0], i[1], i[2], i[3]), solution(i[0], i[1], i[2], i[3])==io_dict[i])
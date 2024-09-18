def solution(prices:list[float], springs:list[int], min_force:int, x:float) -> float:
    min_constant = min_force/x
    spring = springs[0]

    def dfs(i):
        nonlocal spring
        if spring > min_constant: return 0
        if i >= len(springs): return float("INF")

        possible = []

        spring += springs[i]
        possible.append(prices[i]+dfs(i+1))
        spring-=springs[i]
        spring = ((1/spring) + (1/springs[i]))**-1
        possible.append(prices[i]+dfs(i+1))
        spring = springs[i]
        possible.append(prices[i]+dfs(i+1))

        return min(possible)
    
    ans = dfs(1)
    return ans if ans!=float("INF") else -1

from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        print(solution(i[0], i[1], i[2], i[3]), solution(i[0], i[1], i[2], i[3])==io_dict[i])
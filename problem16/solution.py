from functools import cache
def solution(prices:list[float], springs:list[int], min_force:int, x:float) -> float:
    min_constant = min_force/x
    
    @cache
    def rec(ke, bitmask):
        if ke >=min_constant: return 0

        min_cost = float("INF")

        for i in range(len(springs)):
            if bitmask & (1<<i): continue

            price = prices[i]
            k = springs[i]
            new_mask = bitmask | (1<<i)
            min_cost = min(min_cost, price + rec(ke+k, new_mask))

        return min_cost
    
    ans = rec(0, 0)
    return ans if ans!=float("INF") else -1

from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        print(solution(i[0], i[1], i[2], i[3]), solution(i[0], i[1], i[2], i[3])==io_dict[i])
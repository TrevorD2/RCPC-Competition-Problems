def solution(prices:list[float], springs:list[int], min_force:int, x:float) -> float:
    min_constant = min_force/x

    min_price = float("INF")
    for i in range(len(springs)):
        if springs[i] >= min_constant:
            min_price = min(min_price, prices[i])

    return min_price if min_price != float("INF") else -1

from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        print(i)
        print(solution(i[0], i[1], i[2], i[3]), solution(i[0], i[1], i[2], i[3])==io_dict[i])
def solution(prices:list[float], springs:list[int], min_force:int, x:float) -> float:
    min_k = min_force/x
    price_springs = [(prices[i], springs[i]) for i in range(len(prices))]
    min_p = float("inf")

    def recur(remaining, tp, tk):
        nonlocal min_p

        for ps in remaining:
            if tk >= min_k:
                if tp < min_p:
                    min_p = tp
                continue

            n_remaining = remaining.copy()
            n_remaining.remove(ps)
            n_tp, n_tk = tp + ps[0], tk + ps[1]

            recur(n_remaining, n_tp, n_tk)


    recur(price_springs.copy(), 0, 0)
    
    return min_p if min_p != float("inf") else -1

from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        sol = solution(*i)
        print(sol, sol == io_dict[i])


"""
Heres my solution for the problem
idk why u used weird bitmap stuff
this might not be as memory efficient or something (bc i got a mountain of lists here lol) but it seems more readable + clear to me
either way, make sure to update your Constraints + u should remove the 1/t = sum(1/k) series version
also also, make sure to update to use unpacking to pass args - *i intead of i[0], i[1], ...
"""
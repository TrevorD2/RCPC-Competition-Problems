def solution(u: list[int], v: list[int])->int:
    return sum([u[i]*v[i] for i in range(len(u))])

from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        print(solution(i[0],i[1]))

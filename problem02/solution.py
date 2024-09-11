def solution(u: list[int], v: list[int]) -> int:
    return sum([u[i]*v[i] for i in range(len(u))])


from testcases import io_dict
if __name__ == "__main__":
    for inpt in io_dict:
        print(f"{inpt}\n{solution(inpt[0], inpt[1])}\n{solution(inpt[0], inpt[1]) == io_dict[inpt]}\n")


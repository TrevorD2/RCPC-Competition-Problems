def solution(side_length: float) -> int:
    return int(side_length**3 * 19.254 / 1000)


from testcases import io_dict
if __name__ == "__main__":
    for inpt in io_dict:
        print(f"{inpt}\n{solution(inpt)}\n{solution(inpt) == io_dict[inpt]}\n")
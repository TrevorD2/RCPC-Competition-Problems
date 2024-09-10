def solution(side_length: float) -> int:
    return int((side_length**3 * 19.254 / 1000) // 1)

from input_output import io_dict
if __name__ == "__main__":
    for inpt in io_dict:
        print(inpt, solution(inpt), solution(inpt) == io_dict[inpt])

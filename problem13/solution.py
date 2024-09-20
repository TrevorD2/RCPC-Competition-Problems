def solution(landscape: str, start_pos: list[int], start_direction: str) -> list[int]:
    pass


from testcases import io_dict
if __name__ == "__main__":
    for inpt in io_dict:
        sol = solution(inpt)
        print(f"{inpt}\n{sol}\n{sol == io_dict[inpt]}\n")
def solution(participant: str) -> str:
    return "Hello "+participant+", welcome to the RHS Programming Competition!"


from testcases import io_dict
if __name__=="__main__":
    for inpt in io_dict:
        print(f"{inpt}\n{solution(inpt)}\n{solution(inpt) == io_dict[inpt]}\n")
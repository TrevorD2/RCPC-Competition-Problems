def solution(participant: str) -> str:
    return "Hello "+participant+", welcome to the RHS Programming Competition!"

from testcases import io_dict
if __name__=="__main__":
    for i in io_dict:
        print(solution(i), solution(i)==io_dict[i])
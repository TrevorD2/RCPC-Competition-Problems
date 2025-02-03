def solution(landscape_str: str) -> str:
    data = [i.rstrip() for i in landscape_str.split("\n") if i.rstrip()!=""]

    snowflakes = [int(i) for i in data[0]]
    landscape = data[1:]

    def next(grid, snowflakes): 
        bitmask = [min(1, i) for i in snowflakes]



    while max(snowflakes) > 0:
        next(landscape, snowflakes)
        snowflakes = [max(i-1,0) for i in snowflakes]

    return "\n".join(snowflakes)

from testcases import io_dict
if __name__ == "__main__":
    for inpt in io_dict:
        sol = solution(inpt)
        print(f"{inpt}\n\n{sol}\n{sol == io_dict[inpt]}\n")
        print(io_dict[inpt])

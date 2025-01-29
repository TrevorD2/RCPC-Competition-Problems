def solution(landscape_str: str) -> str:
    col_nums = [int(x) for x in landscape_str.split("\n")[0]]
    landscape = [list(row) for row in landscape_str.split("\n")[1:]]

    def next_gen(landscape):

        delta = False

        for y, row in enumerate(landscape):
            for x, char in enumerate(row):
                if char == "*":
                    if landscape[y+1][x] == " ":
                        landscape[y][x] = " "
                        landscape[y+1][x] = "*"
                        delta = True


                    elif landscape[y+1][x] == "/" and landscape[y+1][x-1] == " ":
                        landscape[y][x] = " "
                        landscape[y+1][x-1] = "*"
                        delta = True

                    elif landscape[y+1][x] == "\\" and landscape[y+1][x+1] == " ":
                        landscape[y][x] = " "
                        landscape[y+1][x+1] = "*"
                        delta = True

        if not delta:
            for x, n in enumerate(col_nums):
                if n > 0:
                    col_nums[x] -= 1
                    landscape[0][x] = "*"
                    delta = True

        return delta

    ret = True
    while ret:
        ret = next_gen(landscape)
    
    return "\n".join(["".join(row) for row in landscape])


from testcases import io_dict
if __name__ == "__main__":
    for inpt in io_dict:
        sol = solution(inpt)
        print(f"{inpt}\n\n{sol}\n{sol == io_dict[inpt]}\n")
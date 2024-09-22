def solution(landscape_str: str) -> str:
    col_nums = [int(x) for x in landscape_str.split("\n")[0]]
    landscape = [list(row) for row in landscape_str.split("\n")[1:]]

    def next_gen(landscape):
        for y, row in enumerate(landscape):
            for x, char in enumerate(row):
                if char == "*":
                    if landscape[y+1][x] == " ":
                        landscape[y][x] = " "
                        landscape[y+1][x] = "*"

                    elif landscape[y+1][x] == "/" and landscape[y][x-1] == " ":
                        landscape[y][x] = " "
                        landscape[y][x-1] = "*"

                    elif landscape[y+1][x] == "\\" and landscape[y][x+1] == " ":
                        landscape[y][x] = " "
                        landscape[y][x+1] = "*"

        for x, n in enumerate(col_nums):
            if n > 0:
                col_nums[x] -= 1
                landscape[0][x] = "*"

    last_landscape = ""
    while landscape != last_landscape:
        last_landscape = [row.copy() for row in landscape]
        next_gen(landscape)
    

    return "\n".join(["".join(row) for row in landscape])


from testcases import io_dict
if __name__ == "__main__":
    for inpt in io_dict:
        sol = solution(inpt)
        print(f"{inpt}\n\n{sol}\n{sol == io_dict[inpt]}\n")

        with open("problem13/out.txt", "w") as f:
            f.write(repr(sol))
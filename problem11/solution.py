def solution(funhouse_str: str, start_pos: list[int], start_direction: str) -> list[int]:
    funhouse = funhouse_str.split("\n")
    x, y = start_pos
    dir_str_to_arr = {"up": [0, -1], "down" : [0, 1], "left" : [-1, 0], "right" : [1, 0]}
    dx, dy = dir_str_to_arr[start_direction]

    funhouse_length = len(funhouse[0])
    funhouse_height = len(funhouse)
    
    while 0 <= x < funhouse_length and 0 <= y < funhouse_height:
        print(x, y, funhouse[y][x])
        if funhouse[y][x] in "/\\":
            if dx == 1:
                dx, dy = 0, -1
            elif dx == -1:
                dx, dy = 0, 1
            elif dy == 1:
                dx, dy = -1, 0
            elif dy == -1:
                dx, dy = 1, 0
        if funhouse[y][x] == "\\":
            dx *= -1
            dy *= -1

        x += dx
        y += dy


    return x-dx, y-dy


from testcases import io_dict
if __name__ == "__main__":
    for inpt in io_dict:
        sol = solution(*inpt)
        print(f"{inpt}{str(inpt[0])}\n{sol}\n{sol == io_dict[inpt]}\n")
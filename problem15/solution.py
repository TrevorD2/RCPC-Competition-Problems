def solution(grid: str) -> str:
    last_grid = []
    current_grid = [list(row) for row in grid.split("\n")]
    grid_length, grid_height = len(current_grid[0]), len(current_grid)

    print("\n".join(["".join(row) for row in current_grid]))

    generation_count = 0
    while current_grid != last_grid:
        last_grid = current_grid
        current_grid = next(current_grid, grid_length, grid_height)
        print("-"*15)
        print("\n".join(["".join(row) for row in current_grid]))
        generation_count += 1
    
    return generation_count


def next(grid_arr: str, grid_length: int, grid_height: int):
    next_grid = [[" " for x in range(grid_length)] for y in range(grid_height)]

    for y, row in enumerate(grid_arr):
        for x, char in enumerate(row):
            if x == grid_length-1 or y == grid_height-1:
                continue

            neighbor_pos = ((x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1))
            neighbor_count = 0
            for nx, ny in neighbor_pos:
                neighbor_count += grid_arr[ny][nx] == "*"

            if (neighbor_count == 2 and char == "*") or neighbor_count == 3:
                next_grid[y][x] = "*"
            

    return next_grid



from testcases import io_dict
if __name__ == "__main__":
    for inpt in io_dict:
        gen = solution(inpt)
        print("-"*15 + "\n" + f"{inpt}\n{gen}\n{gen == io_dict[inpt]}\n")
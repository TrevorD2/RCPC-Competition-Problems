def solution(grid: str) -> str:
    grid_length, grid_height = len(grid[0]), len(grid)
    print(next(grid))

def next(grid: str):
    next_grid = 




from testcases import io_dict
if __name__ == "__main__":
    for inpt in io_dict:
        print(f"{inpt}\n{solution(*inpt)}\n{solution(*inpt) == io_dict[inpt]}\n")
def solution(floors: str) -> str:
    def search_path(floor, solution_paths, y, x, letter_history, pos_history):
        npos_to_dir = {(y-1, x) : "U", (y+1, x) : "D", (y, x-1) : "L", (y, x+1) : "R"}
        for ny, nx in npos_to_dir:
            try:
                char = floor[ny][nx]
                n_letter_history = letter_history + npos_to_dir[(ny, nx)]

                if (ny, nx) in pos_history:
                    continue
                if char in "#S":
                    continue
                if char == "X":
                    solution_paths.append((ny, nx, n_letter_history))
                    continue

                n_pos_history = pos_history.copy()
                n_pos_history.add((ny, nx))

                search_path(floor, solution_paths, ny, nx, n_letter_history, n_pos_history)

            except:
                pass

    def search_floor(Sy, Sx, floor, letter_history):
        if "T" in floor:
            T_positions = []
            for y, row in enumerate(floor.split("\n")):
                for x, char in enumerate(row):
                    if char == "T":
                        T_positions.append((y, x))
            
            solution_paths = []
            for Ty, Tx in T_positions:
                floor_ver = floor.replace("T", " ").split("\n")
                floor_ver[Ty] = floor_ver[Ty][:Tx] + "X" + floor_ver[Ty][Tx+1:]

                search_path(floor_ver, solution_paths, Sy, Sx, letter_history, set())
            
            return [(y, x, letter_history + "T") for y, x, letter_history in solution_paths]
        
        else:
            floor_ver = floor.replace("E", "X").split("\n")

            solution_paths = []
            search_path(floor_ver, solution_paths, Sy, Sx, letter_history, set())
            return [(-1, -1, path + "E") for y, x, path in solution_paths]
            


    Sy, Sx = 0, 0
    for y, row in enumerate(floors[0].split("\n")):
        for x, char in enumerate(row):
            if char == "S":
                Sy, Sx = y, x

    this_iteration = [(Sy, Sx, "S")]
    for floor in floors:
        next_iteration = []
        for y, x, letter_history in this_iteration:
            next_iteration.extend(search_floor(y, x, floor, letter_history))

        this_iteration = next_iteration
    
    for y, x, letter_history in this_iteration:
        print(letter_history)

    return min(this_iteration, key = lambda x: len(x[2]))[2]


from testcases import io_dict
if __name__ == "__main__":

    for i in io_dict:
        sol = solution(i)
        print(sol, "=", sol==io_dict[i])
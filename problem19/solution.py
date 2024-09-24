def solution(floors: str) -> str:
    def next_pos(floor, solution_paths, y, x, letter_history, pos_history):
        npos_to_dir = {(y-1, x) : "U", (y+1, x) : "D", (y, x-1) : "L", (y, x+1) : "R"}
        for ny, nx in npos_to_dir:
            try:
                char = floor[ny][nx]
                n_letter_history = letter_history + npos_to_dir[(ny, nx)]

                if (ny, nx) in pos_history:
                    continue
                if char in "#S":
                    continue
                if char == "T":
                    solution_paths.append(n_letter_history)
                    continue

                n_pos_history = pos_history.copy()
                n_pos_history.add((ny, nx))

                next_pos(floor, solution_paths, ny, nx, n_letter_history, n_pos_history)

            except:
                pass


    for floor_str in floors:

        floor = floor_str.split("\n")

        start_y, start_x = 0, 0
        T_positions = []
        for y, row in enumerate(floor):
            for x, char in enumerate(row):
                if char == "S":
                    start_y, start_x = (y, x)
                elif char == "T":
                    T_positions.append((y, x))

        for Ty, Tx in T_positions:
            floor_ver = ("\n".join(floor)).replace("T", " ").split("\n")
            floor_ver[Ty] = floor_ver[Ty][:Tx] + "T" + floor_ver[Ty][Tx+1:]

            solution_paths = []

            next_pos(floor_ver, solution_paths, start_y, start_x, "S", set())
            print(solution_paths)



from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        sol = solution(i)
        #print(sol, "=", sol==io_dict[i])
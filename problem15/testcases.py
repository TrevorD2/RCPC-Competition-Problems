io_dict = {
    '               \n          *    \n         **    \n          **   \n               \n               ' : 40,
    '                    \n                    \n                    \n          **        \n      ***           \n            *       \n               **** \n                    \n                    \n                    ' : 4,
    '                              \n                              \n                              \n                              \n                              \n     **                       \n     **                       \n       **                     \n       **                     \n                              \n                              \n                              \n                              \n                              \n                 *            \n               * *            \n                **            \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              \n                              ' : 49,
    '                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n          *                                       \n        * *                                       \n         **                                       \n                                                  \n                  ***   ***                       \n                                                  \n                *    * *    *                     \n                *    * *    *                     \n                *    * *    *                     \n                  ***   ***                       \n                                                  \n                  ***   ***                       \n                *    * *    *                     \n                *    * *    *                     \n                *    * *    *                     \n                                                  \n                  ***   ***                       \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  \n                                                  ' : 299
}

if __name__ == "__main__":
    w, h = 50, 50
    grid = [[" " for __ in range(w)] for _ in range(h)]



    grid[18][8] = "*"
    grid[19][9] = "*"
    grid[17][10] = "*"
    grid[19][10] = "*"
    grid[18][10] = "*"

    for y in [21, 26, 28, 33]:
        for i in range(3):
            grid[y][18+i] = "*"
        for i in range(3):
            grid[y][24+i] = "*"
    
    for y in [23, 24, 25, 29, 30, 31]:
        for x in [16, 21, 23, 28]:
            grid[y][x] = "*"

    final = ("\n".join(["".join(row) for row in grid]))
    print(final)
    with open("problem15/out.txt", "w") as f:
        f.write(repr(final))
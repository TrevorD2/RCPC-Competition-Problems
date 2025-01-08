io_dict = {
    ('               \n          /  \\ \n               \n               \n               \n          /    \n               \n               \n     /        \\\n               \n             \\/\n               \n               \n               \n               ', (4, 5), "right") : (5, 14),
    ('         /         \\\n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n                    \n/                   \n         /          \n                    \n                    \n\\                  /', (9, 10), "left") : (0, 11)
}

if __name__ == "__main__":
    v = [[" " for x in range(20)] for y in range(15)]
    #v[10][9] = "x"
    v[10][0] = "/"
    v[14][0] = "\\"
    v[14][19] = "/"
    v[0][19] = "\\"
    v[0][9] = "/"
    v[11][9] = "/"


    for i, line in enumerate(v):
        print("".join(line) + "! " + str(i))
    print(repr("\n".join(["".join(val) for val in v])))
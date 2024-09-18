io_dict = {
    '               \n          /  \\ \n               \n               \n               \n    x     /    \n               \n               \n     /        \\\n               \n             \\/\n               \n               \n               \n               ' : 0
}

if __name__ == "__main__":
    v = [[" " for x in range(15)] for y in range(15)]
    v[5][4] = "x"
    v[5][10] = "/"
    v[1][10] = "/"
    v[1][13] = "\\"
    v[10][13] = "\\"
    v[10][14] = "/"
    v[8][14] = "\\"
    v[8][5] = "/"
    print(repr("\n".join(["".join(val) for val in v])))
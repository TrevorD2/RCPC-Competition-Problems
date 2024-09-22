io_dict = {
    '1032210100203101\n                \n                \n                \n                \n       /#\\      \n      /   \\     \n     /     \\    \n    /|     |\\   \n     |     |    \n################' : '                \n                \n                \n                \n       /#\\      \n   ** /   \\**   \n  ***/     \\**  \n  **/|     |\\*  \n* ** |     | * *\n################'
}

if __name__ == "__main__":
    t_case =r"""
1032210100203101




       /#\
      /   \
     /     \
    /|     |\
     |     |
################
"""


    length = len(t_case.split("\n")[1])
    t_case2 = "\n".join([row.ljust(length) for row in t_case[1:-1].split("\n")])
    with open("problem13/out.txt", "w") as f:
            f.write(repr(t_case2))
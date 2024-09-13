grid1 = ""
grid1 += " "*15 + "\n"
grid1 += " "*10 + "*" + " "*4 + "\n"
grid1 += " "*9 + "**" + " "*4 + "\n"
grid1 += " "*10 + "*" + " "*4 + "\n"
grid1 += " "*10 + "**" + " "*3 + "\n"
grid1 += " "*15

io_dict = {
    grid1 : 0
}

print(len(grid1.split("\n")))
for line in grid1.split("\n"):
    print("[" + line + "]", len(line))
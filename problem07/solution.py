def solution(coaster: list[str]) -> float:
    y = float(coaster[0].split("|")[0])
    dy = float(coaster[0].split("|")[0]) - float(coaster[1].split("|")[0])

    beam_length = 0
    for slice in coaster[:-1]:
        y -= dy
        beam_length += slice.count("#")*y

    return beam_length


from testcases import io_dict
if __name__ == "__main__":
    for inpt in io_dict:

        inpt = inpt.split("\n")

        print(f"{inpt}\n{solution(inpt)}\n{solution(inpt) == io_dict[inpt]}\n")

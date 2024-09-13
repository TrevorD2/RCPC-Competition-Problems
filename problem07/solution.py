def solution(coaster: str) -> float:
    slices = coaster.split("\n")
    y = float(slices[0].split("|")[0])
    dy = float(slices[0].split("|")[0]) - float(slices[1].split("|")[0])

    beam_length = 0
    for slice in slices[:-1]:
        y -= dy
        beam_length += slice.count("#")*y

    return beam_length


from testcases import io_dict
if __name__ == "__main__":
    for inpt in io_dict:
        print(f"{inpt}\n{solution(inpt)}\n{solution(inpt) == io_dict[inpt]}\n")

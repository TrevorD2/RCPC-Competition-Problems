def solution(time: int) -> str:
    hours = time // 60
    minutes = time % 60
    am_pm = "am"
    if hours >= 12:
        am_pm = "pm"
    if hours >= 13:
        hours -= 12

    clock_display = f"----------\n|{str(hours).zfill(2)}:{str(minutes).zfill(2)} {am_pm}|\n----------"

    return clock_display

from testcases import io_dict
import random
if __name__ == "__main__":
    for i in range(5):
        inpt = random.randint(1, 1349)
        io_dict[inpt] = solution(inpt)
    print(io_dict)
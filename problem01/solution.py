def solution(side_length: float) -> int:
    return int((side_length**3 * 19.254 / 1000) // 1)


if __name__ == "__main__":
    print(solution(float(input())))

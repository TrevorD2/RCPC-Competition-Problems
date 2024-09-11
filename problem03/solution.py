def solution(u: list[int], v: list[int]) -> int:
    return sum([u[i]*v[i] for i in range(len(u))])

if __name__ == "__main__":
    print(solution(list(map(int, input().split())),list(map(int, input().split()))))

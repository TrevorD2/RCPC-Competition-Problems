def solution(heights: list[int]) -> list[int]:
    dp = [1] * len(heights)

    for i in range(1, len(heights)):
        for j in range(i):
            if heights[i] < heights[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        print(solution(i), solution(i)==io_dict[i])
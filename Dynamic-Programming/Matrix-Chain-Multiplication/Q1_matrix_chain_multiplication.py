# matrix chain multiplication
# hint: you will feel inputs needs to divided in each index and calculate answer


class Solution:
    def recursive_mcm(self, nums: list, start_index: int, end_index: int) -> int:
        if start_index >= end_index:
            return 0

        minimum = float('inf')
        for k in range(start_index, end_index):
            temp_answer = self.recursive_mcm(nums, start_index, k) + self.recursive_mcm(nums, k + 1, end_index) + nums[
                start_index - 1] * nums[k] * nums[end_index]
            if temp_answer < minimum:
                minimum = temp_answer
        return minimum

    def memoization_mcm(self, nums: list, start_index: int, end_index: int, dp) -> int:
        if start_index >= end_index:
            return 0

        if dp[start_index][end_index] != 0:
            return dp[start_index][end_index]

        minimum = float('inf')
        for k in range(start_index, end_index):
            temp_answer = self.memoization_mcm(nums, start_index, k, dp) + self.memoization_mcm(nums, k + 1, end_index,
                                                                                                dp) + nums[
                              start_index - 1] * nums[k] * nums[end_index]

            if temp_answer < minimum:
                minimum = temp_answer
        dp[start_index][end_index] = minimum
        return minimum


if __name__ == '__main__':
    N = 10
    arr = []
    # return self.recursive_mcm(arr, 1, N-1)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    solution = Solution()
    solution.memoization_mcm(arr, 1, N - 1, dp)

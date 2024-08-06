class Solution:

    def recursive_burst_balloons(self, nums: list, start: int, end: int) -> int:
        if start > end:
            return 0

        result = 0
        for k in range(start, end + 1):
            temp = self.recursive_burst_balloons(nums, start, k - 1) + \
                   self.recursive_burst_balloons(nums, k + 1, end) + \
                   nums[start - 1] * nums[k] * nums[end + 1]
            result = max(result, temp)
        return result

    def memoization_burst_balloons(self, nums: list, start: int, end: int, dp) -> int:
        if start > end:
            return 0
        if dp[start][end] != 0:
            return dp[start][end]

        result = 0
        for k in range(start, end + 1):
            temp = self.memoization_burst_balloons(nums, start, k - 1, dp) + \
                   self.memoization_burst_balloons(nums,k + 1,end, dp) + \
                   nums[start - 1] * nums[k] * nums[end + 1]
            result = max(temp, result)
        dp[start][end] = result
        return dp[start][end]


if __name__ == '__main__':
    nums = []
    # extra 1 in both ends
    new_nums = [1]
    new_nums.extend(nums)
    new_nums.append(1)

    # return self.recursive_burst_balloons(new_nums, 1, len(nums))
    dp = [[0 for _ in range(len(nums) + 2)] for _ in range(len(nums) + 2)]
    # return self.memoization_burst_balloons(new_nums, 1, len(nums), dp)
    pass

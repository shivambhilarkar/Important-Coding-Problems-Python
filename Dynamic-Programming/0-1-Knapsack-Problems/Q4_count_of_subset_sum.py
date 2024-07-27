# count of subset sum
# count subsets with given sum in array
# TODO: Wrong output on geeksforgeeks

class Solution:

    def recursive_subset_sum_count(self, arr, n, required_sum) -> int:
        if n == 0 and required_sum == 0:
            return 1
        if n == 0:
            return 0
        if required_sum == 0:
            return 1

        if arr[n - 1] <= required_sum:
            take = self.recursive_subset_sum_count(arr, n - 1, required_sum - arr[n - 1])
            dont_take = self.recursive_subset_sum_count(arr, n - 1, required_sum)
            return take + dont_take
        else:
            result = self.recursive_subset_sum_count(arr, n - 1, required_sum)
            return result


if __name__ == '__main__':
   pass
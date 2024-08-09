from typing import List

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_stock_price = float('inf')
        for stock in prices:
            current_profit = stock - min_stock_price
            max_profit = max(current_profit, max_profit)
            min_stock_price = min(min_stock_price, stock)
        return max_profit

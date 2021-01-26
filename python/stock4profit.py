class Solution:
    def maxProfitFee(self, prices: List[int], fee: int) -> int:
        
	"""
	Best Time to Buy and Sell Stock with Transaction Fee
	You may complete as many transactions as you like, 
	but you need to pay the transaction fee for each transaction. 
	You may not buy more than 1 share of a stock at a time 
	(ie. you must sell the stock share before you buy again.)

	Return the maximum profit you can make.
	"""

        if len(prices)<2:
            return 0
        
        profit = 0
        minprice = prices[0]
        
        for price in prices[1:]:
            if price<minprice:
                minprice = price
            elif price>minprice+fee:
                profit += price-(minprice+fee)
                minprice = price - fee
        return profit

    def maxProfit(self, prices: List[int]) -> int:

	"""
	Best Time to Buy and Sell Stock II
	Design an algorithm to find the maximum profit. 
	You may complete as many transactions as you like 
	(i.e., buy one and sell one share of the stock multiple times).
	"""
        
        if len(prices)<2:
            return 0
        
        profit = 0
        minprice = prices[0]
        
        for price in prices[1:]:
            if price<minprice:
                minprice = price
            elif price>minprice:
                profit += price-minprice
                minprice = price
        return profit

    def maxProfitOne(self, prices: List[int]) -> int:
	"""
	Best Time to Buy and Sell Stock
	You want to maximize your profit by choosing a single day 
	to buy one stock and choosing a different day in the future to sell that stock.

	Return the maximum profit you can achieve from this transaction. 
	If you cannot achieve any profit, return 0.
	"""
        
        if len(prices)<2:
            return 0
        
        profit = 0
        minprice = prices[0]
        
        for price in prices[1:]:
            if price<minprice:
                minprice = price
            elif price>minprice:
                profit = max(profit, price-minprice)
        return profit
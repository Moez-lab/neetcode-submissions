class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit=0
        i=1
        while i <= (len(prices)-1):
            if buy>prices[i]:
                print(f"price-> {prices[i]} price[i+1]{prices[i]}")
                buy= prices[i]
                print(buy)
            if buy<prices[i]:
                sell=prices[i]-buy
                profit=max(profit,sell)
            i+=1
        return profit


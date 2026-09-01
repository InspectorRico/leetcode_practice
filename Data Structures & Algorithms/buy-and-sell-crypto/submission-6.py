class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointers: l = lowest buy price seen, r = current sell price candidate
        l, r = 0, 1
        maxP = 0
        
        # Slide r through all prices, maintain l at minimum encountered
        # Note: r <= len(prices)-1 is equivalent to r < len(prices)
        # Both ensure we only access valid indices [0, len(prices)-1]
        while r <= len(prices) - 1:
            
            if prices[l] < prices[r]:
                # Calculate profit if we sell at r using best buy price at l
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # Found lower price - move buy pointer to this better entry point
                l = r
            
            # r += 1 must be outside if-else: we always scan forward through prices
            # Moving it inside either branch would skip prices or cause stuck iteration
            r += 1
        
        return maxP
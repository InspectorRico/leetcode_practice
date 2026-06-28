class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #rank them by height
        #check for which are the furthest from each other

        areas =  []
        
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                area = min(heights[j], heights[i])  * (j-i)
                areas.append(area)

        return max(areas)
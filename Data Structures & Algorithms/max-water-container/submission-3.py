class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # so this is a 2 d graph and the way we can gauge how to store the most water is by finding 
        # the max viable area that can be held

        #viable area is given by a difference of height where one bar is shorter than the other, so
        #for a height to be viable it should be that one bar is taller than the other 

        #the width is given by subtracting the value of the indexes at which each height bar is
        #represented by

        #we can use a two pointers approach where we find the value of area produced by every single 
        #pair of bars and then add the value of this area to a list and then return the value of the 
        #value from that list 

        areas = 0

        l, r = 0 , len(heights)-1

        while l<r:
            current_height = min(heights[l], heights[r])
            current_width = r-l
            current_area = current_height*current_width
            areas = max(areas, current_area)

                                                            
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return areas 
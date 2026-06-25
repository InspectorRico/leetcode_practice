class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        #the key is the element at the index
        #the value is the element's index

        for i, n in enumerate(nums):
            #j + i = target
            #j = target - i <- this is them in index form 
            #prevDiff = target - n <- this is them in value form

            prevDiff = target - n

            if prevDiff in my_dict:
                return [my_dict[prevDiff], i]
            else:
                my_dict[n] = i
                #the key is the element at the index
                #the value is the element's index
                #Each iteration of the for loop is independent - 
                #the else adds the current number to the dictionary
                # then the loop simply moves to the next index. 
                #There's nothing preventing it from continuing.
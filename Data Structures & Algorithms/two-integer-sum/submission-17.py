class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #wha're my constraints
        # length of array is at least 2 and at most 1000
        # only one valid answer exists

        seen = {}
        #key is the element, value is it's index

        for i, n in enumerate(nums):
            #j + i = target
            #j = target - i
            #magic_number = target - n
            magic_number = target - n

            if magic_number in seen:
                return [seen[magic_number], i]
            else:
                seen[n] = i

        #time complexity is 0(n)
        #space complexity is 0(n)
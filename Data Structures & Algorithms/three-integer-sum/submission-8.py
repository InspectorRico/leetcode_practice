class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. Sort array to use two-pointer technique
        # 2. Iterate through each element as the first number 'a'
        # 3. Use two pointers (l and r) to find pairs that sum to -a
        # 4. Skip duplicate values for 'a' and for the left pointer
        # 5. Move pointers based on sum comparison:
        #    - Sum > 0: move right pointer left
        #    - Sum < 0: move left pointer right
        #    - Sum == 0: found triplet, then move both pointers and skip duplicates

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Since sorted, if a > 0, all remaining numbers are positive
            if a > 0:
                break
            # Skip duplicate first numbers
            if i > 0 and nums[i-1] == nums[i]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                current_sum = nums[l] + nums[r] + a
                
                if current_sum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicates for the left pointer
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif current_sum > 0:
                    r -= 1  # Need smaller sum, move right pointer left
                else:
                    l += 1  # Need larger sum, move left pointer right
                    
        return res
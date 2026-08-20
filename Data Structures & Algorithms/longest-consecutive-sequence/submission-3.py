class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0
        
        for num in nums:
            if (num-1) not in num_set:
                length_of_streak = 1  # Count the current number
                current_num = num
                
                while (current_num + 1) in num_set:
                    current_num += 1
                    length_of_streak += 1
                
                longest_streak = max(longest_streak, length_of_streak)
        
        return longest_streak
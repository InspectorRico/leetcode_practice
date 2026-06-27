class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #index1 + index2 = target
        #index1 != index2
        #always one exact solution
        
        l, r = 0, len(numbers)-1
        
        while l<r:
            while l<r and numbers[l] + numbers[r] < target:
                l+=1
            while l<r and numbers[l] + numbers[r] > target:
                r-=1
                
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
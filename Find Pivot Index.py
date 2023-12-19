class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i + 1:])
            
            if left_sum == right_sum:
                return i
        
        return -1

class Solution:
    def moveZeroes(self, nums: list[int]) -> list:
      index = 0

      for num in nums:
        if num != 0:
          print(num, index)
          nums[index] = num
          index += 1
      print(nums)

        
      while index < len(nums):
        nums[index] = 0
        index += 1

      return nums
sks = Solution()
print(sks.moveZeroes([0,1,0,3,12]))  #output=[1,3,12,0,0]

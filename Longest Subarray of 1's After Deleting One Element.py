class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        answer = 0
        left = 0

        zeroes = 0
        ones = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
                while zeroes > 1:
                    if nums[left] == 0:
                        zeroes -= 1
                    else:
                        ones -= 1
                    left += 1
            else:
                ones += 1

            answer = max(answer, ones)

        return answer if zeroes == 1 else answer - 1

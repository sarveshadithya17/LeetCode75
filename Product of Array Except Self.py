from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize two arrays to store the product of elements to the left and right of each element.
        left_products = [1] * n #[1,1,1,1]
        right_products = [1] * n #[1,1,1,1]
        
        # Calculate the product of elements to the left of each element.
        left_product = 1
        for i in range(1, n):   #(1,3)
            left_product *= nums[i - 1]     
            left_products[i] = left_product     #[1,1,2,6] 
        
        # Calculate the product of elements to the right of each element.
        right_product = 1
        for i in range(n - 2, -1, -1):  
            right_product *= nums[i + 1]         
            right_products[i] = right_product       #[24,12,4,1]
        
        # Calculate the final product excluding the current element.
        answer = [left_products[i] * right_products[i] for i in range(n)]   #[24,12,8,6]
        
        return answer

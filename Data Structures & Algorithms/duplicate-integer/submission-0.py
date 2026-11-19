from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    
        unique_elements = set()


        for num in nums:
            
            if num in unique_elements:
                return True

            unique_elements.add(num)
        
        return False

solution = Solution()
nums = [1, 2, 3, 4, 1]
print(solution.hasDuplicate(nums))  

nums = [1, 2, 3, 4, 5]
print(solution.hasDuplicate(nums)) 

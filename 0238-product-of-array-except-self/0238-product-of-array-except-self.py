class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post = nums[len(nums)-1]
        answer = [1 for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            answer[i] *= nums[i-1] * answer[i] * answer[i-1]
            
            
        for i in range(len(nums) - 2, -1, -1):
            answer[i] *= post
            post *= nums[i]
            
        return answer
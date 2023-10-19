class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1
        
        while (left <= right):
            if nums[left] < nums[right]:
                res = min(nums[left], res)
                break
                
            mid = (left + right) // 2
            res = min(nums[mid], res)
            
            if (nums[mid] < nums[right]):
                right = mid - 1
            else:
                left = mid + 1
        return res
                            
                
                
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minProd = 1
        maxProd = 1
        
        for n in nums:
            if n == 0:
                minProd = 1
                maxProd = 1
            temp = n * maxProd
            maxProd = max(temp, n * minProd, n)
            minProd = min(temp, n * minProd, n)
            
            if res < maxProd:
                res = maxProd
                
        return res
        
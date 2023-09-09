class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax = 1 
        curMin = 1
        for n in nums:
            if n == 0:
                curMax = 1
                curMin = 1
                continue
            tmp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            if curMax > res:
                res = curMax
        return res


        
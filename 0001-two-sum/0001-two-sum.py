class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        ans = []
        for i, val in enumerate(nums):
            hmap[val] = i
                
        for i, val in enumerate(nums):
            currtarget = target - val
            if currtarget in hmap.keys() and hmap[currtarget] != i:
                return [i, hmap[currtarget]]
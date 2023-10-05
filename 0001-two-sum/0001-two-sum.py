class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
                
        for i, val in enumerate(nums):
            if target - val in hmap.keys() and hmap[target - val] != i:
                return [i, hmap[target - val]]
            else:
                hmap[val] = i
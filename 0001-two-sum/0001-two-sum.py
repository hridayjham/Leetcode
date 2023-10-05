class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        ans = []
        for i in range(len(nums)):
            ##if nums[i] not in hmap.keys():
                hmap[nums[i]] = i
                
        for i in range(len(nums)):
            currtarget = target - nums[i]
            if currtarget in hmap.keys() and hmap[currtarget] != i:
                ans.append(i)
                ans.append(hmap[currtarget])
                return ans
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxVol, curVol = 0, 0
        
        while (l < r):
            lowerheight = min(height[l], height[r])
            curVol = (r - l) * lowerheight
            if curVol > maxVol:
                maxVol = curVol
            if height[l] == lowerheight:
                l += 1
                while height[l] < lowerheight and l < r:
                    l += 1
            else:
                r -= 1
                while (height[r] < lowerheight) and l < r:
                    r -= 1
        return maxVol
            
        
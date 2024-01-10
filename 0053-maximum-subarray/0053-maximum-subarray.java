class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int curSum = 0;
        int n = nums.length;
        
        for(int i = 0; i<n; i++) {
            if (curSum < 0)
                curSum = 0;
            curSum = curSum + nums[i];
            
            maxSum = Math.max(curSum, maxSum);
        }
        return maxSum;
    }
}
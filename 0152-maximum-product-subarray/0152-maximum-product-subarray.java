import java.util.Arrays;
class Solution {
    public int maxProduct(int[] nums) {
        int res = Arrays.stream(nums).max().getAsInt();
        int curMax = 1;
        int curMin = 1;
        int n = nums.length;
        
        for(int i = 0; i < n; i++) {
            int x = nums[i];
            if (x == 0) {
                curMax = 1;
                curMin = 1;
            }
            
            int a = x * curMax;
            int b = x * curMin;
            curMax = Math.max(Math.max(a, b), x);
            
            curMin = Math.min(Math.min(a, b), x);
                
            if (curMax > res)
                res = curMax;
        }
        
        return res;
    }
}
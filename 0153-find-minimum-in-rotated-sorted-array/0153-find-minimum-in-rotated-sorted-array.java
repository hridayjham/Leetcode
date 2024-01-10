import java.util.Arrays;
class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        
        return Arrays.stream(nums).min().getAsInt();
        
        
    }
}
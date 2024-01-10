class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] prefix = new int[n];
        int[] postfix = new int[n];
        int[] result = new int[n];
        prefix[0] = 1;
        postfix[n-1] = 1;
        for(int i = 0; i<n-1; i++) {
            prefix[i+1] = prefix[i] * nums[i];
        }
        for(int i = n - 2; i>=0; i--) {
            postfix[i] = postfix[i + 1] * nums[i + 1];
        }
        
        for(int i = 0; i<n; i++) {
            result[i] = prefix[i] * postfix[i];
        }
        return result;
    }
}
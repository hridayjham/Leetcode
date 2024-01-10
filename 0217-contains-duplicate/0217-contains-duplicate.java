class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        boolean flag = false;
        int n = nums.length;
        
        for(int i = 0; i < n; i++) {
            if (map.containsKey(nums[i])) {
                return true;
            }
            map.put(nums[i], i);
        }
        return false;
    }
}
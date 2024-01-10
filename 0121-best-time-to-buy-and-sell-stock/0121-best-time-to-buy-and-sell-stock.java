class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int left = 0;
        int right = 1;
        int maxP = 0;
        while(left < right && right < n) {
            if(prices[right] - prices[left] <= 0) {
                left = right;
                right++;
            }
            else if (prices[right] - prices[left] > maxP) {
                maxP = prices[right] - prices[left];
                right++;
            }
            else {
                right++;
            }
        }
        return maxP;
    }
}
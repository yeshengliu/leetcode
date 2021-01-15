class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxNum = 0;  // Maximum number of consecutive 1s
        int currNum = 0;  // Maximum number of consecutive 1s in current search
        
        for (int num: nums) {
            if (num == 1) {
                currNum += 1;
            } else {
                maxNum = Math.max(maxNum, currNum);
                currNum = 0;
            }
        }
        maxNum = Math.max(maxNum, currNum);
        
        return maxNum;
        
    }
}
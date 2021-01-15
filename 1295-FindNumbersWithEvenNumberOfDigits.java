class Solution {
    public int findNumbers(int[] nums) {
        
        int count = 0;  // Count numbers that have even number of digits
        
        for (int num: nums) {
            int numDigits = 1;
            while (num >= 10) {
                numDigits += 1;
                num /= 10;
            }
            if (numDigits % 2 == 0) {
                count += 1;
            }
        }
        
        return count;
        
    }
}
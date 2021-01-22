class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        int length = nums.length;
        
        while (i < length) {
            if (nums[i] == val) {
                nums[i] = nums[length - 1];
                length -= 1;
            } else {
                i += 1;
            }
        }
        return length;
    }
}
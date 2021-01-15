class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] squared = new int[nums.length];
        int curr = 0;  // index to insert new value into squared
        
        // Find the value from nums that is closest to 0
        int startValue = nums[0];
        int startIndex = 0;
        for (int i = 1; i < nums.length; i++) {
            if (Math.abs(nums[i]) < Math.abs(startValue)) {
                startValue = nums[i];
                startIndex = i;
            }
        }
        
        // Start insertion from startIndex
        // Compare sqrt(startIndex - 1) & sqrt(startIndex) and move on...
        int pointerA = startIndex - 1;
        int pointerB = startIndex;
        while (pointerA >= 0 || pointerB < nums.length) {
            if (pointerA < 0) {
                squared[curr] = (int) Math.pow(nums[pointerB], 2);
                pointerB += 1;
            } else if (pointerB >= nums.length) {
                squared[curr] = (int) Math.pow(nums[pointerA], 2);
                pointerA -= 1;
            } else if (Math.abs(nums[pointerA]) < Math.abs(nums[pointerB])) {
                squared[curr] = (int) Math.pow(nums[pointerA], 2);
                pointerA -= 1;
            } else {
                squared[curr] = (int) Math.pow(nums[pointerB], 2);
                pointerB += 1;
            }
            curr += 1;
        }
        
        return squared;
    }
}
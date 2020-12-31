class Solution {
    public int maxArea(int[] height) {
        int front = 0;
        int end = height.length - 1;
        int maxArea = Math.min(height[front], height[end]) * (end - front);
        while (front < end) {
            if (height[front] < height[end]) {
                front++;
            } else {
                end--;
            }
            maxArea = Math.max(maxArea, Math.min(height[front], height[end]) * (end - front));
        }
        return maxArea;
    }
}
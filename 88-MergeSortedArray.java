class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (n > 0) {
            int pointerM = m - 1;
            int pointerN = n - 1;
            int pointerInsert = m + n - 1;
            while (pointerM >= 0 && pointerN >= 0) {
                if (nums1[pointerM] > nums2[pointerN]) {
                    nums1[pointerInsert] = nums1[pointerM];
                    pointerM -= 1;
                } else {
                    nums1[pointerInsert] = nums2[pointerN];
                    pointerN -= 1;
                }
                pointerInsert -= 1;
            }
            System.arraycopy(nums2, 0, nums1, 0, pointerN + 1);
        }
    }
}
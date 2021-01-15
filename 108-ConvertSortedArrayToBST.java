/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) return null;
        if (nums.length == 1) return new TreeNode(nums[0], null, null);
        int i = (int) nums.length / 2; // Root of BST
        return new TreeNode(nums[i], 
                            sortedArrayToBST(Arrays.copyOfRange(nums, 0, i)),
                            sortedArrayToBST(Arrays.copyOfRange(nums, i + 1, nums.length)));
    }
}
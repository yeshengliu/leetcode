class SparseVector {
    
    HashMap<Integer, Integer> values = new HashMap<>();
    
    SparseVector(int[] nums) {
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                values.put(i, nums[i]);
            }
        }
        
    }
    
	// Return the dotProduct of two sparse vectors
    public int dotProduct(SparseVector vec) {
        int total = 0;
        for (int k: vec.values.keySet()) {
            if (this.values.containsKey(k)) {
                total += this.values.get(k) * vec.values.get(k);
            }
        }
        return total;
    }
}

// Your SparseVector object will be instantiated and called as such:
// SparseVector v1 = new SparseVector(nums1);
// SparseVector v2 = new SparseVector(nums2);
// int ans = v1.dotProduct(v2);
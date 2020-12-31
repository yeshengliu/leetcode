class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> merged = new ArrayList<>();
        int[] curr = intervals[0];
        for (int[] interval: intervals) {
            if (interval[0] > curr[1]) {
                merged.add(curr);
                curr = interval;
            }
            if (interval[1] > curr[1]) {
                curr[1] = interval[1];
            }
        }
        merged.add(curr);
        return merged.toArray(new int[merged.size()][]);
    }
}
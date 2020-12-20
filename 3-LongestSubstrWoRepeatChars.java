class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int i = 0, j = 0, output = 0;
        Set<Character> seen = new HashSet<>();
        while (i < n && j < n) {
            if (!seen.contains(s.charAt(j))) {
                seen.add(s.charAt(j));
                j += 1;
                output = Math.max(output, j - i);
            } else {
                seen.remove(s.charAt(i));
                i += 1;
            }
        }
        return output;
    }
}
class Solution {
    
    private int start, end = 0;
    
    public String longestPalindrome(String s) {
        int len = s.length();
        if (len < 2) {
            return s;
        }
        for (int i = 0; i < len; i++) {
            findPalindrome(s, i, i);
            findPalindrome(s, i, i + 1);
        }
        return s.substring(start, end + 1);
    }
    
    private void findPalindrome(String s, int i, int j) {
        while (i >= 0 && j <= s.length() - 1) {
            if (s.charAt(i) == s.charAt(j)) {
                if ((j - i) > (end - start)) {
                    start = i;
                    end = j;
                }
                i--;
                j++;
            } else {
                break;
            }
        }
    }
}
// Last updated: 6/25/2025, 4:12:25 AM
import java.util.HashMap;

class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> romanMap = new HashMap<>();
        romanMap.put('I', 1);
        romanMap.put('V', 5);
        romanMap.put('X', 10);
        romanMap.put('L', 50);
        romanMap.put('C', 100);
        romanMap.put('D', 500);
        romanMap.put('M', 1000);

        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i + 1 < s.length() && romanMap.get(s.charAt(i)) < romanMap.get(s.charAt(i + 1))) {
                res += romanMap.get(s.charAt(i + 1)) - romanMap.get(s.charAt(i));
                i++; // Skip the next character
            } else {
                res += romanMap.get(s.charAt(i));
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "IX";
        System.out.println(solution.romanToInt(s)); // Output: 9
    }
}

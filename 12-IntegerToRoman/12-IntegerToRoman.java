// Last updated: 6/25/2025, 4:12:32 AM
import java.util.LinkedHashMap;
import java.util.Map;

class Solution {
    public String intToRoman(int num) {
        // Define a LinkedHashMap to store the integer values and their corresponding Roman numerals
        Map<Integer, String> romanMap = new LinkedHashMap<>();
        romanMap.put(1000, "M");
        romanMap.put(900, "CM");
        romanMap.put(500, "D");
        romanMap.put(400, "CD");
        romanMap.put(100, "C");
        romanMap.put(90, "XC");
        romanMap.put(50, "L");
        romanMap.put(40, "XL");
        romanMap.put(10, "X");
        romanMap.put(9, "IX");
        romanMap.put(5, "V");
        romanMap.put(4, "IV");
        romanMap.put(1, "I");
        
        StringBuilder result = new StringBuilder();
        
        // Iterate over the map entries
        for (Map.Entry<Integer, String> entry : romanMap.entrySet()) {
            int key = entry.getKey();
            String value = entry.getValue();
            
            while (num >= key) {
                result.append(value);
                num -= key;
            }
        }
        
        return result.toString();
    }
}
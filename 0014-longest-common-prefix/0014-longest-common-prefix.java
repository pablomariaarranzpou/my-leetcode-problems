class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        List<String> strings = Arrays.asList(strs);    
        String longest = strings.stream().min(Comparator.comparingInt(String::length)).get();
        int min = longest.length();
        String actual = "";
        
        for(int i = 0; i < min; i++){
            char starting = strs[0].charAt(i);
            for(int j = 1; j < strs.length; j++){
                
                if(starting != strs[j].charAt(i)){
                    return actual;
                }
                
            }
            actual += starting;
        }
        return actual;
    }
}
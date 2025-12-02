/*
 * @lc app=leetcode.cn id=76 lang=java
 *
 * [76] 最小覆盖子串
 */

// @lc code=start
class Solution {
    Map<Character, Integer> tMap = new HashMap<>();
    Map<Character, Integer> map = new HashMap<>();

    public String minWindow(String s, String t) {
        int l = 0, r = 0, len = Integer.MAX_VALUE;
        int resL = -1, resR = -1;

        for(int i = 0; i < t.length(); i++)
            tMap.put(t.charAt(i), tMap.getOrDefault(t.charAt(i), 0) + 1);
        
        while(l <= r && r < s.length()){
            if(tMap.containsKey(s.charAt(r)))
                map.put(s.charAt(r), map.getOrDefault(s.charAt(r), 0) + 1);

            while(check() && l <= r){
                if(r - l + 1 < len){
                    len = r - l + 1;
                    resL = l;
                    resR = r;
                }

                if(tMap.containsKey(s.charAt(l)))
                    map.put(s.charAt(l), map.getOrDefault(s.charAt(l), 0) - 1);
                
                l++;
            }

            r++;
        }

        return len > 0 ? s.substring(resL, resR + 1) : "";
    }

    public boolean check(){
        Iterator iter = tMap.entrySet().iterator();

        while(iter.hasNext()){
            Map.Entry entry = (Map.Entry)iter.next();
            Character key = (Character)entry.getKey();
            Integer val = (Integer)entry.getValue();

            if(map.getOrDefault(key, 0) < val)
                return false;
        }

        return true;
    }
}
// @lc code=end


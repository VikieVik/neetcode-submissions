class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # make sure lenght of both input is same to proceed to next steps 
        if len(s) != len(t):
            return False
        
        # maintain frequency of each letter in hashmap
        map_s, map_t = {}, {}

        for i in range(len(s)):
            map_s[s[i]] = map_s.get(s[i], 0) + 1
            map_t[t[i]] = map_t.get(t[i], 0) + 1

        # check if the hashmaps length matches
        return map_t == map_s

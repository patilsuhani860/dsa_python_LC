class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
            
        map_st = {}
        map_ts = {}
        
        for ch1, ch2 in zip(s, t):
            if ch1 in map_st:
                if map_st[ch1] != ch2:
                    return False
            else:
                map_st[ch1] = ch2
                
            if ch2 in map_ts:
                if map_ts[ch2] != ch1:
                    return False
            else:
                map_ts[ch2] = ch1
                
        return True

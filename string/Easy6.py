class Solution(object):
    def isPalindrome(self, s):
        s=s.strip().lower()
        t=[]
        scopy=[]
        for i in range(len(s)):
            if 'a'<=s[i]<='z' or '0'<=s[i]<='9':
                scopy.append(s[i])
        for i in range(len(s)):
            if 'a'<=s[len(s)-1-i]<='z' or '0'<=s[i]<='9':
                t.append(s[len(s)-1-i])
        if t==scopy:
            return True
        else:
            return False
        
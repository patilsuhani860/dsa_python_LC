class Solution(object):
    def strStr(self, haystack, needle):
            if len(haystack)>=len(needle):
                return haystack.find(needle)
            else:
                return -1

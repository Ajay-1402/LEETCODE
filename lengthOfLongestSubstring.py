class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        maxLen = 0
        for i in range(len(s)):
            b = set()
            b.add(s[i])
            for j in range( i+1, len(s) ):
                if s[j] in b:
                    break
                else:
                    b.add(s[j])

            if len(b) > maxLen:
                maxLen = len(b)
        return maxLen    

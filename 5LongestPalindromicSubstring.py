class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <=1:
            return s
        if len(s) ==2:
            if s[0] == s[1]:
                return s
        result = []
        isPalindromic = [[False for i in range(len(s))] for i in range(len(s))]
        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         if s[j] == s[i]:
        #             isPalindromic[i][j] = True

        for j in range(len(s)):
            for i in range(j+1):
                if j-i<2:
                    isPalindromic[i][j] = (s[i] == s[j])
                else:
                    isPalindromic[i][j] = (s[j] == s[i] and isPalindromic[i+1][j-1])

                if isPalindromic[i][j] and j+1-i > len(result):
                    result = s[i:j+1]
        return result


inputvalue = "abcda"
s = Solution()
t = s.longestPalindrome(inputvalue)
print(t)
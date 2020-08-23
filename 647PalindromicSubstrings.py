class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.result = 0
        self.isPalindrome = [[False for i in range(len(s))] for i in range(len(s))]
        self.dfs(s)
        return self.result
    
    def dfs(self,s):
        for R in range(len(s)):
            for L in range(R+1):
                if R-L <2: 
                    self.isPalindrome[L][R] = s[R] == s[L]
                if L < len(s)-1 and s[R] == s[L] and self.isPalindrome[L+1][R-1]:
                    self.isPalindrome[L][R] = True
                if self.isPalindrome[L][R]:
                    self.result+=1
                    

       
inputvalue = "aaa"
s = Solution()
count = s.countSubstrings(inputvalue)
print(count)
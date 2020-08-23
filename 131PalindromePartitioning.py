class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.result = []
        self.dfs(s,[])
        return self.result


    # def GetPalindrome(self,array):
    #     for s in array:
    #         if len(s) <= 1: continue
    #         isPalindrome = [[False for i in range(len(s))] for i in range(len(s))]
    #         for R in range(len(s)):
    #             for L in range(R+1):
    #                 if R-L < 2:
    #                     isPalindrome[L][R] = s[R] == s[L]
    #                 else:
    #                      isPalindrome[L][R] = s[R] == s[L] and isPalindrome[L+1][R-1]
    #                 if isPalindrome[L][R] and R-L>0:
    #                     array.remove(s)
    #                     if L > 0:
    #                         array.append(s[0:L])
    #                     array.append(s[L:R+1])
    #                     if R < len(s)-1:
    #                         array.append(s[R+1:len(s)])
            
    #         return self.GetPalindrome(array)
    # def GetPalindrome(self):
    #     for s in self.result:
    #         if len(s) <= 1: continue
    #         isPalindrome = [[False for i in range(len(s))] for i in range(len(s))]
    #         for R in range(len(s)):
    #             for L in range(R+1):
    #                 if R-L < 2:
    #                     isPalindrome[L][R] = s[R] == s[L]
    #                 else:
    #                      isPalindrome[L][R] = s[R] == s[L] and isPalindrome[L+1][R-1]
    #                 if isPalindrome[L][R] and R-L>0:
    #                     self.result.remove(s)
    #                     if L > 0:
    #                         self.result.append(s[0:L])
    #                     self.result.append(s[L:R+1])
    #                     if R < len(s)-1:
    #                         self.result.append(s[R+1:len(s)])
    #                     return
    def dfs(self,s,temp):
        if not s:
            self.result.append(temp[:])
            return
        for i in range(1,len(s)+1):
            if self.isPalindrome(s[:i]):
                temp.append(s[:i]) 
                self.dfs(s[i:],temp)
                temp.pop()


    def isPalindrome(self,s):
        return s == s[::-1]
        

class Solution_own(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
    
    def isPalin(self,s):
        L = 0
        R = len(s)-1
        while L<R:
            if s[L] == s[R]:
                L+=1
                R-=1
            else:
                return False
        return True



inputvalue = "aab"
s = Solution()
res = s.partition(inputvalue)
print(res)

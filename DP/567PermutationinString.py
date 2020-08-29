
from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2:str):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        self.s1permutation = []
        used = [False]*len(s1)
        self.dfs(s1,"",used)
        if len(s1) > len(s2):
            return False
        if len(s1) == len(s2) ==1:
            return s1 == s2
        for i in range(len(s2)-1):
            t = s2[i:i+len(s1)]
            if t in self.s1permutation:
                return True
        return False

    def dfs(self,s1,temp,used):
        if len(temp) == len(s1):
            self.s1permutation.append(temp[:])
        for i in range(len(s1)):
            if used[i]: continue
            if i > 0 and s1[i] == s1[i-1] and used[i-1] : continue
            temp+=s1[i]
            used[i] = True
            self.dfs(s1,temp,used)
            temp = temp[:-1]
            used[i] = False

    def checkInclusion2(self, s1, s2:str):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        if len(s1) == len(s2) ==1:
            return s1 == s2
        counter1 = Counter(s1)
        counter2 = Counter()
        for i in range(len(s2)):
            counter2[s2[i]]+=1
            if counter2 == counter1:
                return True
            if i+1 >= len(s1):
                element = s2[i+1-len(s1)]
                if counter2[element] == 1:
                    del counter2[element]
                else:
                    counter2[element] -= 1
                # temp = s2[i+1-len(s1):i+1]
                # tempcounter = Counter(temp)
        return False

s1 = "adc"
s2 = "dcda"
s= Solution() 
res = s.checkInclusion2(s1,s2)
print(res)
            


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s0 = []
        t0 = []
        for i in range(len(S)):
            if S[i] == "#":
                if len(s0) > 0:
                    s0.pop()
            else:
                s0.append(S[i])
        
        for j in range(len(T)):
            if T[j] == "#":
                if len(t0) > 0:
                    t0.pop()
            else:
                t0.append(T[j])
        return s0 == t0


S = "a##c"
T = "#a#c"
s = Solution()
r = s.backspaceCompare(S,T)
print(r)
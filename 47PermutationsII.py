class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        if len(nums) <=1:
            self.result.append(nums)
            return self.result
        self.used = [False]*len(nums)
        self.dfs(sorted(nums),[])

    def dfs(self,nums,temp):
        if len(temp) >= len(nums):
            self.result.append(temp[:])
        for i in range(len(nums)):
            if self.used[i]: continue
            if i>0 and nums[i] == nums[i-1] and self.used[i-1]: continue
            temp.append(nums[i])
            self.used[i] = True
            self.dfs(nums,temp)
            temp.pop()
            self.used[i] =False

inputvalue = [1,1,2]
s = Solution()
s.permuteUnique(inputvalue)
for item in s.result:
    print(item)
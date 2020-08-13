class Solution(object):
    result = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return nums
        self.dfs(nums,[])
        return self.result

    def dfs(self,nums,tempArray):
        if len(tempArray) == len(nums):
            self.result.append(tempArray[:])
        for i in range(len(nums)):
            if nums[i] in tempArray:
                continue
            tempArray.append(nums[i])
            self.dfs(nums,tempArray)
            tempArray.pop()
        

inputvalue = [1,2,3]
s = Solution()
res = s.permute(inputvalue)
for item in res:
    print(item)                            
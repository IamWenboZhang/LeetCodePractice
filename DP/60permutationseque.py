class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = []
        for i in range(n):
            nums.append(str(i+1))
        k-=1
        self.result = ""
        #caculate permuation counts for each length of list
        pcounts = [1]
        for i in range(1,n+1):
            pcounts.append(pcounts[i-1]*i)
        self.caculatepermuatation(nums,pcounts,k)
        return self.result

    def caculatepermuatation(self,nums: list, permuations: list, k: int):
        if len(nums) <= 0:
            return
        currentindex = int(k / permuations[len(nums)-1])
        num = nums[currentindex]
        self.result += num
        nextk = k%permuations[len(nums)-1]
        nums.remove(num)
        self.caculatepermuatation(nums,permuations,nextk)


n = 4
k = 9
s=Solution()
res = s.getPermutation(n,k)
print(res)
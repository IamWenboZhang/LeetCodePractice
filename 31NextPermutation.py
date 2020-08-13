class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        firstSmall = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                firstSmall = i
                break

        if firstSmall == -1:
            self.reverse(nums,0,len(nums)-1)
            return
        for j in range(len(nums)-1,-1,-1):
            if nums[j] > nums[firstSmall]:
                nums[j],nums[firstSmall] = nums[firstSmall],nums[j]
                break
        
        self.reverse(nums,firstSmall+1,len(nums)-1)
        
            
            
        

    def reverse(self,nums,L,R):
        while(L<R):
            nums[L],nums[R] = nums[R],nums[L]
            L+=1
            R-=1

inputvalue = [1]
s = Solution()
s.nextPermutation(inputvalue)
print(inputvalue)
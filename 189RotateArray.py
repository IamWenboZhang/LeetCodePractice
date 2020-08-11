class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)

    def reverse(self,nums,L,R):
        while(L<R):
            nums[L],nums[R] = nums[R],nums[L]
            L+=1
            R-=1
    

def main():
    inputvalue = [1,2,3,4,5,6,7]
    s = Solution()
    s.rotate(inputvalue,3)

    for item in inputvalue:
        print(item)

main()
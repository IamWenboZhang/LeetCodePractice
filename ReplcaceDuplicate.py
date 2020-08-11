class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                continue
            nums[count] = nums[i]
            count += 1
        return count


def main():
    InputValue = [1,1,2]
    s = Solution()
    length = s.removeDuplicates(InputValue)
    for i in range(length):
        print(InputValue[i])
   

main()
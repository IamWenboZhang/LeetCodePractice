class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__nums__ = nums
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.__nums__ [i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        for index in range(i,j):
            res += self.__nums__[index]
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
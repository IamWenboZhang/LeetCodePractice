class Solution:

    # def reverse(self, x: int) -> int:
    #     if x < 2**31*-1 or x > 2**31-1:
    #         return 0        
    #     value = str(x)
    #     isFu = False
    #     if value[0] == '-':
    #         value = value[1:len(value)]
    #         isFu = True
    #     if value[len(value)-1] == '0' and len(value) > 1:
    #         value = value[0:len(value)-1]
    #     result = str()
    #     for i in range(len(value)):
    #         result += value[-(i+1)]        
    #     if isFu:
    #         result = '-' + result
    #     if int(result)< 2**31*-1 or int(result) > 2**31-1:
    #         return 0
    #     return int(result)
    def reverse(self, x: int) -> int:
        symbol = 1 if x > 0 else -1
        temp = str(x)[::-1]
        temp1 = str(x)[::5]
        print(temp)

solution = Solution()
solution.reverse(15342364690)


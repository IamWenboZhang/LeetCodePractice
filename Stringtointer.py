class Solution(object):
    
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        resultstr = ""
        foundsign = False
        hasdigital = False
        for i in range(len(str)):
            if(str[i] == ' ' and not foundsign and not hasdigital):
                continue
            else:                
                if (str[i] == '-' or str[i] == '+') and not foundsign :
                    resultstr += str[i]
                    foundsign = True
                else:
                    if str[i] >='0' and str[i]<='9':
                        hasdigital = True
                        resultstr += str[i]
                    else:
                        break
        if not hasdigital:
            return 0
        result = int(resultstr)
        if result>2**31-1:
            return 2**31-1
        if result<2**31*-1:
            return 2**31*-1
        return result

def main():
    inputvalue = "2147483648"
    soulution = Solution()
    intvalue = soulution.myAtoi(inputvalue)
    
    print (intvalue)

main()

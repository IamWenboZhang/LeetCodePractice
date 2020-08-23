class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # for i in range(n):
        #     self.NQueen(0,n,[])
        queens = [0]*n
        self.result = []
        self.NQueen(0,n,queens)
        return self.result
    
    def NQueen(self,row,n,queens):
        if row >= n: 
            print("\n")
            self.printResult(queens)
            return
        for columnindex in range(n):
            rowindex = 0
            while rowindex < row:
                if queens[rowindex] == columnindex or abs(queens[rowindex] - columnindex) == abs(rowindex - row):
                    break
                rowindex+=1
            if rowindex == row:
                queens[row] = columnindex
                self.NQueen(row+1,n,queens)

    def printResult(self,queens):
        onesolution = []
        for row in range(len(queens)):
            rowcontent = ""
            for i in range(0,queens[row]):
                rowcontent += (".")
            rowcontent +=("Q")
            for i in range(queens[row]+1,len(queens)):
                rowcontent += (".")
            onesolution.append(rowcontent)
            print(rowcontent)
        self.result.append(onesolution)
            

inputvalue = 8
s = Solution()
s.solveNQueens(inputvalue)
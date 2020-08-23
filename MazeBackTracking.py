class Solution(object):
    def findPath(self, startX,startY,endX,endY,maze):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.rolad = [[0 for i in range(len(maze))]for i in range(len(maze))] 
        self.tryMove(startX,startY,endX,endY,maze)
        return self.rolad
    
    def tryMove(self,currentX,currentY,endX,endY,maze):
        # if current postion is end return true
        if currentX == endX and currentY == endY:
            self.rolad[currentX][currentY] = 1
            return True
        if currentX < len(maze) and currentY < len(maze) and currentX >=0 and currentY >=0:
            # check current postion is wall or not
            if maze[currentX][currentY] == 1:
                self.rolad[currentX][currentY] = 0
                return False
            else:
                self.rolad[currentX][currentY] = 1
                # move down
                if self.tryMove(currentX+1,currentY,endX,endY,maze):
                    return True           

                # move right
                if self.tryMove(currentX,currentY+1,endX,endY,maze):
                    return True

                self.rolad[currentX][currentY] = 0
                return False


maze= [[0,1,1,0,0],
[0,1,1,0,0],
[0,0,0,0,1],
[0,0,1,0,0],
[1,0,1,0,1]]

startX = 0
startY = 0
endX = 3
endY = 4

s = Solution()
r = s.findPath(startX,startY,endX,endY,maze)
for item in r:
    print(item)
    print("\n")

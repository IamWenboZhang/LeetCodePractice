class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        self.result = []
        self.orignal = []
        for i in range(m):
            self.orignal.append(i+1)
        for item in queries:
            self.moveitem(item,self.orignal)

    def getindex(self,array,forfind):
        i = -1
        for item in array:
            i+=1
            if item == forfind:
                return i
                
        
    def moveitem(self,key,_orinal):
        position = self.getindex(_orinal,key)  
        if position > -1 and position < len(_orinal) :  
            temp = _orinal[position]
            self.result.append(position)
            for i in range(position,0,-1):
                _orinal[i] = _orinal[i-1]
            _orinal[0] = temp

inputvalue = [7,5,5,8,3]
s = Solution()
s.processQueries(inputvalue,8)
print(s.result)


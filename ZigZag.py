def converttoZigZag(s:str,rownums:int):
    if rownums == 1:
        return s
    
    rows = [None]*rownums
    for j in range(rownums):
        rows[j] = ""

    for i in range(len(s)):
        index = i%(rownums*2-2)
        index = index if index<rownums else (rownums*2-2)-index
        rows[index] += s[i]
    
    result = ""
    for x in range(rownums):
        result += rows[x]
    
    return result

def main():
    teststr = "Paypalishiring"
    after = converttoZigZag(teststr,4)
    print(after)

main()
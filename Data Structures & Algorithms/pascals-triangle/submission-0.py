class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            print(i)
            temp = []
            for j in range(len(res[i]) + 1):
                print(i, j)
                if j == 0 or j == len( res[i] ):
                    temp.append(1)
                else:
                    temp.append(res[i][j-1] + res[i][j])
            res.append(temp)
            temp = []
        
        return res
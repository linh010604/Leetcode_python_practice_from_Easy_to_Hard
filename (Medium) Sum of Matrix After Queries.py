class Solution(object):
    def matrixSumQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: int
        """
        col = list()
        row = list()
        numrow = 0
        numcol = 0
        res = 0
        
        for i in range (n) :
            col.append(0)
            row.append(0)
            
        for i in range (len(queries) - 1 , -1 , -1) :
            if queries[i][0] == 0 and row[queries[i][1]] == 0:
                numrow += 1
                row[queries[i][1]] = 1
                res += queries[i][2] * (n - numcol)
            if queries[i][0] == 1 and col[queries[i][1]] == 0:
                numcol += 1
                col[queries[i][1]] = 1
                res += queries[i][2] * (n - numrow)
                
        return res
                
        

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) ==0:
            return(False)
        
        elif len(matrix) ==1:
            if not matrix[0]:
                return(False)
            elif target in matrix[0]:
                return(True)
            else:
                return(False)
        
        for row in range(len(matrix)):
            if matrix[row][0] == target:
                return(True)
            elif target> matrix[row][0]:
                if target in matrix[row]:
                    return(True)
        return(False)
            
        
                
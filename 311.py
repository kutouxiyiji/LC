class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        def transpose(B):
            res = []
            for j in range(len(B[0])):
                temp = []
                for i in range(len(B)):
                    temp.append(B[i][j])
                res.append(temp)
            return(res)
        
        def multiply(a,b):
            res = 0
            for i in range(len(a)):
                res += a[i]*b[i]
            return(res)
        res = []
        B_t = transpose(B)
        for i in range(len(A)):
            a = A[i]
            temp = []
            for j in range(len(B_t)):
                b = B_t[j]
                temp.append(multiply(a,b))
            res.append(temp)
        return(res)
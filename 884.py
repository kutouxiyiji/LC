class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A.split(' ')
        B = B.split(' ')
        t = A +B
        d = collections.Counter(t).items()
        res= []
        for x,v in d:
            if v==1:
                res.append(x)
        return(res)
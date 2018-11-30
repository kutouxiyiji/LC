class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result = 0
        for i in range(len(S)):
            if S[i] in J:
                result +=1
        return(result)
        
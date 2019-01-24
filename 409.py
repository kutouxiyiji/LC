class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = collections.Counter(s)
        flag = 0
        res = 0
        for v in d.values():
            if v%2 == 1:
                if flag ==0:
                    flag =1
                    res +=v-1
                else:
                    res += v-1
            else:
                res +=v
        return(res+flag)
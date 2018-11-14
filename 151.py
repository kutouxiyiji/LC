class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        temp = s.split(' ')
        res =''
        for item in temp[::-1]:
            if item != '':
                r= item + ' '
                res +=r
        return(res[:-1])
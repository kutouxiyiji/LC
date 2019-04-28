class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k>=len(num):
            return('0')
        stack = []
        for x in num:
            while stack and stack[-1] > x and k:
                stack.pop()
                k -= 1
            stack.append(x)
        
        
        if len(num) == 0:
            return "0"
        else:
            return str(int(''.join(stack[:len(stack)-k])))
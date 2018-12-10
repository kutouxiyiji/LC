class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        a=collections.Counter(ransomNote)
        m=collections.Counter(magazine)
        for item in a:
            if item not in m:
                return(False)
            if item in m and a[item]>m[item]:
                return(False)
        return(True)
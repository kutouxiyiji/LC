import string
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet =  list(string.ascii_lowercase)
        d = dict()
        for i in range(len(alphabet)):
            d[alphabet[i]] = morse[i]
        res = []
        for word in words:
            res.append('')
            for i in range(len(word)):
                res[-1] += d[word[i]]
        return(len(set(res)))
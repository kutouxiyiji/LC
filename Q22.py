# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:35:45 2017

@author: ktxyj
"""

class solution():
    def generateHELPer(self, LEFT, RIGHT, item, res):
        if RIGHT < LEFT:
            return
        if LEFT==0 and RIGHT==0:
            res.append(item)
        if LEFT > 0:
            self.generateHELPer(LEFT - 1, RIGHT, item + "(", res)
        if RIGHT > 0:
            self.generateHELPer(LEFT, RIGHT - 1, item + ")", res)
            
    def Generater(self, n):
        if n == 0:
            return([])
        res = []
        self.generateHELPer(n, n, '', res)
        return(res)
    
    
if __name__ == '__main__':    
    S = solution()
    print(S.Generater(4))
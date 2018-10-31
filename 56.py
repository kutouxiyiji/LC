# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 22:03:48 2018

@author: yongw
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

#        intervals.sort(key=lambda x: x.start)
        q = []
        res = []
        for i in range(len(intervals)):
            q.append([intervals[i].start, 0])
            q.append([intervals[i].end, 1])
        q.sort(key= lambda x:(x[0], x[1]))
#        print(q)
#        j = 0
        S = E =0 # count the number of start and end
        for j in range(len(q)): # j is the index of q
            if S==0 and q[j][1] == 0:
                S +=1
                start = q[j][0]
            elif S!=0 and q[j][1] == 0:
                S+=1
            elif q[j][1]==1 and S!=E:
                E+=1
                end = q[j][0]
            if S==E and S!=0:
                res.append([start, end])
                S = E =0
        return(res)
        
            
            
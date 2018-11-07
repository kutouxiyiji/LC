# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 00:54:14 2017

@author: KTXYJ
"""


def isValid(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            stack.append(s[i])
        if s[i] == ')':
            if stack == [] or stack.pop() != '(':
                return(False)
        if s[i] == ']':
            if stack == [] or stack.pop() != '[':
                return(False)
        if s[i] == '}':
            if stack == [] or stack.pop() != '{':
                return(False)
    if stack:
        return(False)
    else:
        return(True)
            

if __name__ == '__main__':
    s ='[({()})]()'
    print(isValid(s))
    
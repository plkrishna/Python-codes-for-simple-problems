#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:28:20 2020

@author: plkrishna2211
"""

class tree:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=None
        self.left=None
    @classmethod
    def create_tree(self,arr, root, i, n):   
        if i < n: 
            temp = tree(arr[i])  
            root = temp  
            root.left = self.create_tree(arr, root.left, 2 * i + 1, n)  
            root.right = self.create_tree(arr, root.right,2 * i + 2, n) 
        return root 
    def left_in(self,val=0):
        if self.left!=None:
            return False
        else:
            k=tree(val)
            self.left=k
            return True
    def right_in(self,val=0):
        if self.right!=None:
            return False
        else:    
            k=tree(val)
            self.right=k
            return True
    def bfs(self):
        que=[self]
        while que!=[]:
            print(que[0].val)
            h=que.pop(0)
            if h.left!=None:
                que.append(h.left)
            if h.right!=None:
                que.append(h.right)
                

ne=tree.create_tree([1,5,2,3,6,7,4],None,0,7)
ne.bfs()
            
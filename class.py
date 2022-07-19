# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 12:58:25 2022

@author: ELCOT
"""
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        
        
point=Point(10,20)
print(point.x)

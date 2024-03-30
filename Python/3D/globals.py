# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 23:24:23 2019

@author: hutton
"""
import os

def initialize(casenumber): 
    global IP,txt
    IP = os.path.join(os.getcwd(),"../../Data/"+ casenumber +"/path")
    print(os.getcwd())
    txt = os.path.join(os.getcwd(),"../3D/center.txt") 
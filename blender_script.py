# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 22:39:22 2022

@author: sayori
"""
import bpy
import pickle




def get_model(filename='D:/data_structure/03/maze.pkl'):
    with open(filename,'rb') as f:
        a=pickle.load(f)
    w,h=a.shape
    for i in range(w):
        for j in range(h):
            if a[i][j]==0:
                bpy.ops.mesh.primitive_cube_add(location=(2*i,2*j,0))
                
get_model()
            



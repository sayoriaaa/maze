# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:31:16 2022

@author: sayori
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def rmove():
    ret=[0,0]
    choice=np.random.choice([1,-1])
    pos=np.random.choice([0,1])
    ret[pos]=choice
    return ret

    

def gen(width=10,height=10):
    def valid_move(i,j):
        cnt=0
        plane[i][j]=8
        while(cnt<1000):
            cnt+=1
            pos=rmove()
            if i+2*pos[0]<0 or j+2*pos[1]<0 or i+2*pos[0]>2*width or j+2*pos[1]>2*height:
                continue
            if plane[i+2*pos[0]][j+2*pos[1]]==1 and plane[i+pos[0]][j+pos[1]]==0:
                plane[i+pos[0]][j+pos[1]]=8
                valid_move(i+2*pos[0],j+2*pos[1]) 
        return 
    
    plane=np.zeros((width*2+1,height*2+1),dtype=np.int8) 
    for i in range(1,2*width):
        for j in range(1,2*height):
            if i%2==1 and j%2==1:
                plane[i][j]=1 
                
    print(plane)
    valid_move(1,1)
    return plane

def maze_show_path(a):
    sns.heatmap(a,cmap='GnBu')
    plt.show()
    
    



pa=gen(width=18,height=16)
maze_show_path(pa)
    
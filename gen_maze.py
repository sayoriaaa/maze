# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:31:16 2022
@author: sayori
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


def rmove():
    ret=[0,0]
    choice=np.random.choice([1,-1])
    pos=np.random.choice([0,1])
    ret[pos]=choice
    return ret

class Maze:
    def __init__(self,width=10,height=10,method=0):
        self.w=width
        self.h=height
        if method==0:
            self.maze=gen1(width=self.w,height=self.h)
        self.terminant=set_terminant(self.maze)
        print(self.terminant)
        
    def solve_re(self):
        def valid_move(i,j):
            cnt=0
            plane[i][j]=4
            if i==self.terminant[0] and j==self.terminant[1]:
                return True
            while(cnt<1000):
                cnt+=1
                pos=rmove()
                if i+pos[0]<0 or j+pos[1]<0 or i+pos[0]>2*width or j+pos[1]>2*height:
                    continue
                if plane[i+pos[0]][j+pos[1]]==8:
                    if valid_move(i+pos[0],j+pos[1]):
                        return True
            plane[i][j]+=8#显示走进死胡同的路
            return False
        
        plane=self.maze.copy()
        width,height=self.w,self.h  
        if not valid_move(1,1):
            print('no solution')
        else:
            print('solution found')
            self.solution=plane
        
        
    def maze_show_path(self):
        sns.heatmap(self.maze,cmap='GnBu')
        plt.show()
    
    def maze_show_solution_path(self):
        sns.heatmap(self.solution,cmap='GnBu')
        plt.show()
    
    def maze_show_wall(self):
        a=self.maze.copy()
        w,h=a.shape
        for i in range(1,w-1):
            for j in range(1,h-1):
                if a[i][j]==8:
                    a[i][j]=0
                else:a[i][j]=8
        sns.heatmap(a,cmap='GnBu')
        plt.show()
        
    def maze_save(self,filename='maze.pkl'):
        with open(filename,'wb') as f:
            pickle.dump(self.maze,f)
        
        
        
            

    

def gen1(width=10,height=10):
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
    valid_move(1,1)
    return plane

def set_terminant(a):
    w,h=a.shape
    for i in range(h-2,1,-1):
        if a[w-2][i]==8:
            return w-2,i
        

        


    
    
    
    


a=Maze(width=20,height=20)
a.solve_re()
a.maze_show_solution_path()
a.maze_save()

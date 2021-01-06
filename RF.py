#!/usr/bin/python3

from mpl_toolkits import mplot3d
import numpy as np
import math
import random

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import time

class manipulator:

        def __init__(self, l1, l2, l3, l4):
                self.l1 = float(l1)
                self.l2 = float(l2)
                self.l3 = float(l3)
                self.l4 = float(l4)
                self.pos = np.array([0.0,0.0,0.0])
                self.angle = np.array([0.0,0.0,0.0,0.0,0.0]) 
                self.fk()

        def fk(self):   
            q1 = self.angle[0] 
            q2 = self.angle[1] 
            q3 = self.angle[2] 
            q4 = self.angle[3] 
            q5 = self.angle[4] 
            l1 = self.l1 
            l2 = self.l2 
            l3 = self.l3 
            l4 = self.l4 
            
            px = np.cos(q1)*(-l4*np.sin(q1+q2+q3) + l3*np.cos(q2+q3) + l2*np.cos(q2)) 
            py = np.sin(q1)*(-l4*np.sin(q1+q2+q3) + l3*np.cos(q2+q3) + l2*np.cos(q2)) 
            pz = l1 - l2*np.sin(q2) - l3*np.cos(q2+q3) - l4*np.cos(q1+q2+q3) 
            
            self.pos = np.array([px, py, pz])

        def ik(self, pos):
            l1 = self.l1 
            l2 = self.l2 
            l3 = self.l3 
            l4 = self.l4 
            
            q1 = atan2(pos[1], pos[0])

class trajectory:
        def __init__(self, startpos, endpos, nump):
                self.s = startPos
                self.f = endPos
                self.path = np.empty((num, 3), float)


#def animate():


def main():

        print("Enter length of linkages:")
        l1 = 5 #input("L1: ")
        l2 = 5 #input("L2: ")
        l3 = 5 #input("L3: ")
        l4 = 5 #input("L4: ")

        sLink = manipulator(l1,l2,l3,l4)

        pos = np.array([[]])

        
        fp = open("plt.txt","w+" )
       
#        fig = plt.figure()
#        plt.ion()
#        ax = plt.axes(projection='3d')

        for a in range(10):
           # sLink.angle[0] = a*0.9
            sLink.angle[1] = a*(90/10.0) #random.randint(0,90)
            
            for b in range(10):
                sLink.angle[2] = b*(90/10.0)  #random.randint(0,90)
                
                for c in range(10): 
                    sLink.angle[3] = c*(90/10.0) #random.randint(0,90)
                    
                    for d in range(10):
                        sLink.angle[4] = d*(90/10.0) #random.randint(0,90)
                        sLink.fk()
                        fp.write(str(sLink.pos[0]) + ' ' + str(sLink.pos[1]) + ' ' + str(sLink.pos[2]) + '\n')
                        #fp.write(str(sLink.pos.tolist())+'\n')
                        pos = np.append(pos, sLink.pos)
                       # plt.scatter(sLink.pos[0], sLink.pos[1], sLink.pos[2]) 
       
        pos = np.reshape(pos,(-1,3)) 
        print(pos)
        fp.close()
#        x,y,z = pos[0:,0], pos[0:,1], pos[0:,2]
#        ax.scatter3D(x, y, z)
#        ax.set_xlabel('X Label')
#        ax.set_ylabel('Y Label')
#        ax.set_zlabel('Z Label')
#        plt.show(block=True)

        print(sLink.l1)
        print(sLink.l2)   
        print(sLink.l3)
        print(sLink.l4)

if __name__ == "__main__":
        main()


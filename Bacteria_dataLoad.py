#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 14:13:38 2017

@author: duarteocarmo
"""

#IMPORT RELEVANT LIBRARIES

import pandas as pd
import numpy as np


def dataLoad(filename):
    
#    IMPORT FILE
    
    rawdata=np.loadtxt(filename)
     
    print("The initial file has {} lines.".format(rawdata.shape[0]))
    
#    CREATE A MATRIX EQUAL TO RAWDATA  BUT FILLED WITH ZEROS
    
    allzeros=np.zeros(rawdata.shape)
    
    print("Starting Analysis...")
    
#    START LOOP
    
    for i in range(rawdata.shape[0]):
        
#        ANALYSE TEMPERATURE VALUE, IF BAD, LINE VALUES=1 AND WARN USER
        
        if rawdata[i,0]>60 or rawdata[i,0]<10:
            print("Unexpected temperature value in line {}.".format(i))
            allzeros[i,:]=1
                   
#        ANALYSE GROWTH RATE VALUES, IF BAD, LINE VALUES=1 AND WARN USER         
                 
        if rawdata[i,1]<0:
            print("Unexpected growth rate value in line {}.".format(i))
            allzeros[i,:]=1
                 
#        ANALYSE EXPERIMENT ID, IF BAD, LINE VALUES=1         
                   
        if rawdata[i,2] not in [1, 2, 3, 4]:
            print("Unexpected bacteria type in line {}.".format(i))
            allzeros[i,:]=1
                 
#        IF ROW DOESNT GET CAUGT UP, LINE VALUES REMAIN 1 AND WARN USER         
                   
        else:
            pass
        
    print("Analysis Complete!")
    
    
#    FINAL FILE IS=THE RAW DATA MATRIX(WHERE THE ZEROS MATRIX, IS STILL ZERO
    
    output=rawdata[allzeros==0]
    
#    RESHAPING OF OUTPUT
    
    data=output.reshape(-1,3)
    
    print("The final file has {} lines.".format(data.shape[0]))
    
    return data

    


    
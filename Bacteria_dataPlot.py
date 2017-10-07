#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 10:20:22 2017

@author: duarteocarmo
"""

import matplotlib.pyplot as plt
import numpy as np


def dataPlot(data):
    
#    NUMBER OF BACTERIA DATA--------------------------------------------------

    bacteriatypes=np.arange(1,5)                    #Vector with all the bacteria types
   
    bacteriainfile=data[:,2]                        #Vector corresponding to last column of data file

    ones=bacteriainfile[bacteriainfile==1].size     #Frequency of 1

    twos=bacteriainfile[bacteriainfile==2].size     #Frequency of 2

    threes=bacteriainfile[bacteriainfile==3].size   #Frequency of 3

    fours=bacteriainfile[bacteriainfile==4].size    #Frequency of 4

    frequency=np.array([ones,twos,threes,fours])    #Create vector of frequencies

#    NUMBER OF BACTERIA PLOT---------------------------------------------------

    width = 1/1.5
    plt.bar(bacteriatypes,frequency, width, color="blue")
    plt.xticks(np.arange(min(bacteriatypes), max(bacteriatypes)+1, 1.0))
    plt.title("Number of Bacteria Present in Data")
    plt.xlabel("Bacteria Types")
    plt.ylabel("Frequency")
    plt.show()
    
#    GROWTH RATE BY TEMPERATURE DATA-------------------------------------------

    rightorder=data[data[:,0].argsort()]            #Matrix order by growing temperatures
    
#    data[data[:,0].argsort()][:,0]
    

    bacteriainfile=rightorder[:,2]                  #get array with all bacteria types
    temperaturesinfile=rightorder[:,0]              #get array with all temperatures
    ratesinfile=rightorder[:,1]                     #get array with all rates



    temp1=temperaturesinfile[bacteriainfile==1]     #Get temperatures for bacteria type 1
    rate1=ratesinfile[bacteriainfile==1]            #Get rates for bacteria type 1
   
    temp2=temperaturesinfile[bacteriainfile==2]     #repeat for other types.  
    rate2=ratesinfile[bacteriainfile==2]            
    
    temp3=temperaturesinfile[bacteriainfile==3]     
    rate3=ratesinfile[bacteriainfile==3]
    
    temp4=temperaturesinfile[bacteriainfile==4]     
    rate4=ratesinfile[bacteriainfile==4]

#    GROWTH RATE BY TEMPERATURE PLOT-------------------------------------------

    plt.plot(temp1, rate1,"b-", label="Salmonella enterica")
    plt.plot(temp2, rate2,"r-", label="Bacillus Cereus")
    plt.plot(temp3, rate3,"g-", label="Listeria")
    plt.plot(temp4, rate4,"m-", label="Brochothrix thermosphacta")
    plt.legend(loc="upper left")
    plt.title("Growth rate by temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Growth Rate")
    plt.xlim([0, 60])
    plt.grid()
    plt.show()




    
    


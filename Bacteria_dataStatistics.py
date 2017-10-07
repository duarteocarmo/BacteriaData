#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 08:20:09 2017

@author: duarteocarmo
"""

import numpy as np

def dataStatistics(data, statistic):
    
#    CONVERT INPUT STRING TO LOWER CASE

    statistic=statistic.lower()
       
#    GET MEAN TEMPERATURE
    
    if statistic=="mean temperature":
        result=(np.sum(data,axis=0)[0])/(data.shape[0])
#        print("The Mean Temperature is {}.".format(result))
   
#    GET MEAN GROWTH RATE
    
    if statistic=="mean growth rate":
        result=(np.sum(data,axis=0)[1])/(data.shape[0])
#        print("The Mean Growth rate is {}.".format(result))
        
#        GET STANDART DEVIATION OF TEMPERATURE
    
    if statistic=="std temperature":
        result=np.std(data[:,0])
#        print("Standard deviation of Temperature is {}.".format(result))  
        
#        GET STANDART DEVIATION OF GROWTH RATE
        
    if statistic=="std growth rate":
        result=np.std(data[:,1])
#        print("Standard deviation of Growth Rate is {}.".format(result))  
        
#        GET NUMBER OF ROWS
        
    if statistic=="rows":
        result=data.shape[0]
#        print("The total number of rowns in the data is {}.".format(result))
        
#        GET MEAN OF RATES WHERE TEMP IS LOWER THEN 20
        
    if statistic=="mean cold growth rate":
        goodtemp=data[data[:,0] < 20]
        getrate=goodtemp[:,1]
        result=np.mean(getrate)
#        print("The Mean Cold Growth rate is {}.".format(result))
        
#        GET MEAN OF RATES WHERE TEMP IS HIGHER THEN 50
        
    if statistic=="mean hot growth rate":
        goodtemp=data[data[:,0] > 50]
        getrate=goodtemp[:,1]
        result=np.mean(getrate)
#        print("The Mean Hot Growth rate is {}.".format(result))

    if statistic!="mean hot growth rate" and statistic!="mean cold growth rate" and statistic!="rows" and statistic!="std growth rate" and statistic!="std temperature" and statistic!="mean growth rate" and statistic!="mean temperature":
        result=0
        print("Sorry, the statistic you entered does not exist.")
        
    return result
    
    
    
#print(dataStatistics(data,"Mean Temperature"))
#print(dataStatistics(data,"Mean Growth rate"))
#print(dataStatistics(data,"Std Temperature"))
#print(dataStatistics(data,"Std Growth rate"))
#print(dataStatistics(data,"Rows"))
#print(dataStatistics(data,"Mean Cold Growth rate"))
#print(dataStatistics(data,"Mean Hot Growth rate"))
#print(dataStatistics(data,"duarte"))
    
    
    
    
    
    
    
    
    
    
    


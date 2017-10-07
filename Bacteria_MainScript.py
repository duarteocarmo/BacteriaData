#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 18:06:12 2017

@author: duarteocarmo
"""

import numpy as np

from Bacteria_dataLoad import dataLoad
from Bacteria_dataPlot import dataPlot
from Bacteria_dataStatistics import dataStatistics
from Bacteria_displayMenu import displayMenu

print("Welcome to Bacteria Data Analysis! Here are your options:")
menuItems = np.array(["Load Data;", "Filter Data (Or clean filters);", "Display Statistics;", "Generate Plots;", "Quit;"])
filters = np.array(["Filter Growth Rates;", "Select a bacteria;","Filter Temperatures(a bit more);","Delete all filters;"])
bacteriatypes = np.array(["Salmonella enterica;", "Bacillus Cereus;", "Listeria;", "Brochothrix thermosphacta;"])
filename = ""

while True:                                                                                                             #start menu
    choice = displayMenu(menuItems) 
    
#    LOAD DATA
    
    if choice == 1:
        while True:
            try:                
                filename=input("Please enter the name of your data file ensuring that you type .txt afterwards: ")
                rawdata=dataLoad(filename)                                                                              #run dataload function with file requested
            except IOError:               
                print("Sorry, we could not find your file,please try again: ")                                          #if error, ask again
            else:
                break   

#    FILTER DATA
                                                                                                                        #if good, stop. 
    elif choice == 2:                
        if filename == "":
            print("A file must be loaded first. Start by choosing option 1.")            
        else:
            filterchoice=displayMenu(filters)                                                                           #if filter, displaymenu filter options
            
            #    RATE FILTER
            
            if filterchoice == 1:
                while True:
                    try:
                        lowerbound=float(input("Enter the LOWER Bound for the rate filter: "))
                        upperbound=float(input("Enter the UPPER Bound for the rate filter: "))
                    except ValueError:
                        print("Sorry, it looks like what you entered was not a number,please try again: ")
                    else:
                        break  
                applylow=rawdata[rawdata[:,1]>lowerbound]                                                               #extract part of matrix that has rates biiger than lowerbound
                applyhigh=applylow[applylow[:,1]<upperbound]
                rawdata=applyhigh          
                
                 #    BACTERIA FILTER
                
            if filterchoice ==2:
                
                bacteriachoice=displayMenu(bacteriatypes)
                
                if bacteriachoice == 1:
                    rawdata=rawdata[rawdata[:,2] == 1]                                                                  #extract matrix where last column has value of number selected in bacteria menu.
                    print("Filter Successful.")
                
                if bacteriachoice == 2:
                    rawdata=rawdata[rawdata[:,2] == 2] 
                    print("Filter Successful.")
                
                if bacteriachoice == 3:
                    rawdata=rawdata[rawdata[:,2] == 3] 
                    print("Filter Successful.")
                
                if bacteriachoice == 4:
                    rawdata=rawdata[rawdata[:,2] == 4] 
                    print("Filter Successful.")     

                 #    TEMPERATURE FILTER
                             
            if filterchoice == 3:
                while True:
                    try:
                        lowerbound=float(input("Enter the LOWER Bound for the temperature filter: "))
                        upperbound=float(input("Enter the UPPER Bound for the temperature filter: "))
                        
                    except ValueError:
                        print("Sorry, it looks like what you entered was not a number,please try again: ")
                        
#                        maybe separate
                    else:
                        break 
                    
                applylow=rawdata[rawdata[:,0]>lowerbound]
                applyhigh=applylow[applylow[:,0]<upperbound]
                rawdata=applyhigh  
                
                 #    CLEAR ALL FILTERS
                
            if filterchoice ==4:
                rawdata=dataLoad(filename)
                print("All filters have been cleared.")
                
#    DISPLAY STATISTICS
                
    elif choice == 3:        
        if filename == "":
            print("A file must be loaded first. Start by choosing option 1.") 
        else:
            while True:
                try:                
                    statistic=input("Please enter the name of the statistic: ")
                    print("{} is equal to {}.".format(statistic,dataStatistics(rawdata, statistic)))                    #run dataStatistics function
                except IOError:               
                    print("Sorry, the statistic you entered does not exist, please try again: ")
                else:
                    break   
                
#    GENERATE PLOTS 
                
    elif choice == 4:        
        if filename == "":
            print("A file must be loaded first. Start by choosing option 1.") 
        else:
            while True:
                try:                
                    dataPlot(rawdata)                                                                                    #run plot function
                except IOError:               
                    print("Sorry. Something went wrong. ")
                else:
                    break
                
#GET OUT
                
    elif choice == 5:
        print("It was nice having you.Goodbye.")
        break
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 20:32:35 2023

@author: emiliomartinez 

This is to find the similarites between austin gomber and blake snell 
#need to put data into sql db nect tine 
"""

import pandas as pd 
import numpy as np 
import pybaseball as pyb
import sqlite3
import matplotlib as mpl
import matplotlib.patches as patches
from matplotlib import pyplot as plt
from tabulate import tabulate

#get the 2022 statcast data
data2022 = pyb.statcast('2022-04-01', '2022-10-30') 

#get all the data for Gomber and Snell from the 2022 season
gomber = data2022.loc[data2022['player_name'] == 'Gomber, Austin'] 
snell = data2022.loc[data2022['player_name'] == 'Snell, Blake'] 


#combined = pd.concat([gomber,snell], axis = 0) 

gomber1 = gomber[['player_name','pitch_type','release_speed','release_pos_x','p_throws','pfx_x','pfx_z','release_spin_rate','release_extension','release_pos_y','pitch_name','spin_axis']]
snell1 = snell[['player_name','pitch_type','release_speed','release_pos_x','p_throws','pfx_x','pfx_z','release_spin_rate','release_extension','release_pos_y','pitch_name','spin_axis']]

#change the movment to inches and from the pitchers' perspective, 
gomber1['pfx_x'] = gomber1['pfx_x'] *-12 
gomber1['pfx_z'] = gomber1['pfx_z'] *12  
gomber1['release_pos_y'] = gomber1['release_pos_y'] /12  
snell1['release_pos_y'] = snell1['release_pos_y'] /12  
snell1['pfx_x'] = snell1['pfx_x'] *-12 
snell1['pfx_z'] = snell1['pfx_z'] *12 


#group data by pitchy type and rename columns
z=gomber1.groupby('pitch_type').mean()
z.rename(columns = {'release_speed':'Velocity','release_pos_x':'Release Side (ft.)','pfx_x':'Horizontal Movement (in.)','pfx_z':'Vertical Movement (in.)','release_spin_rate':'Spin Rate','release_extension':'Extension (ft.)','release_pos_y':'Release Height (ft.)','spin_axis':'Spin Axis'}, inplace = True)
w=snell1.groupby('pitch_type').mean()
w.rename(columns = {'release_speed':'Velocity','release_pos_x':'Release Side (ft.)','pfx_x':'Horizontal Movement (in.)','pfx_z':'Vertical Movement (in.)','release_spin_rate':'Spin Rate','release_extension':'Extension (ft.)','release_pos_y':'Release Height (ft.)','spin_axis':'Spin Axis'}, inplace = True)

#reorder columns and decided to drop spin rate
z = z[['Velocity', 'Vertical Movement (in.)','Horizontal Movement (in.)', 'Release Height (ft.)' ,'Release Side (ft.)','Extension (ft.)','Spin Axis' ]] 
w = w[['Velocity', 'Vertical Movement (in.)','Horizontal Movement (in.)', 'Release Height (ft.)' ,'Release Side (ft.)','Extension (ft.)','Spin Axis' ]] 

print('')
print("Gomber 2022 Averages")
print('')
print(z.to_markdown()) 
print('')
print('')
print("Snell 2022 Averages")
print('')
print(w.to_markdown())

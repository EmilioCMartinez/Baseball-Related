#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 20:37:29 2022

@author: emiliomartinez
"""

import pybaseball as pyb 
from pybaseball import statcast  
import pandas as pd   
import matplotlib.pyplot as plt 

#look up Emmanuel Clase player id 
clase = pyb.playerid_lookup("Clase")

#create a df that only has Emmannuel Clase data from 2022
clase_new = pyb.statcast_pitcher('2022-01-01','2022-06-26', player_id = 661403) 

#only get sliders from the data set
clase_sliders = clase_new.loc[clase_new.pitch_name.str.contains('Slider', na = False)] 

#only get cutters from the data set
clase_cutters = clase_new.loc[clase_new.pitch_name.str.contains('Cutter', na = False)] 


#put all pitches (only sliders from here on out) in velo buckets
clase_sliders.loc[(clase_sliders['release_speed'] >= 87) & (clase_sliders['release_speed'] <= 90),'velo_bucket'] = '88-90'
clase_sliders.loc[(clase_sliders['release_speed'] >= 90) & (clase_sliders['release_speed'] <= 92),'velo_bucket'] = '90-92'
clase_sliders.loc[(clase_sliders['release_speed'] >= 92) & (clase_sliders['release_speed'] <= 94),'velo_bucket'] = '92-94'
clase_sliders.loc[(clase_sliders['release_speed'] >=94) & (clase_sliders['release_speed'] <= 97),'velo_bucket'] = '94-96'


#------------------------------------------------------------------------------------------------------------------------------------------------------------
#create histograms of horizontal release position and frequency, colored by velo buckets

clase_sliders[clase_sliders['velo_bucket'] == '88-90'].release_pos_x.plot(kind='hist', color='red', edgecolor='black', alpha=1.0, figsize=(10, 7))
clase_sliders[clase_sliders['velo_bucket'] == '90-92'].release_pos_x.plot(kind='hist', color='blue', edgecolor='black', alpha=0.5, figsize=(10, 7))
clase_sliders[clase_sliders['velo_bucket'] == '92-94'].release_pos_x.plot(kind='hist', color='yellow', edgecolor='black', alpha=0.2, figsize=(10, 7))
clase_sliders[clase_sliders['velo_bucket'] == '94-96'].release_pos_x.plot(kind='hist', color='lime', edgecolor='black', alpha=0.9, figsize=(10, 7))

plt.legend(labels=['88-90', '90-92','92-94','94-96'])
plt.title('Clase (2022) Distribution of Velo by  Horizontal Release Position', size=24)
plt.xlabel('Horizontal Release Position', size=18)
plt.ylabel('Frequency', size=18);


#create histograms of vertical release position and frequency, colored by velo bukets


clase_sliders[clase_sliders['velo_bucket'] == '88-90'].release_pos_z.plot(kind='hist', color='red', edgecolor='black', alpha=1.0, figsize=(10, 7))
clase_sliders[clase_sliders['velo_bucket'] == '90-92'].release_pos_z.plot(kind='hist', color='blue', edgecolor='black', alpha=0.5, figsize=(10, 7))
clase_sliders[clase_sliders['velo_bucket'] == '92-94'].release_pos_z.plot(kind='hist', color='yellow', edgecolor='black', alpha=0.2, figsize=(10, 7))
clase_sliders[clase_sliders['velo_bucket'] == '94-96'].release_pos_z.plot(kind='hist', color='lime', edgecolor='black', alpha=0.9, figsize=(10, 7))

plt.legend(labels=['88-90', '90-92','92-94','94-96'])
plt.title('Clase (2022) Distribution of Velo by  Vertical Release Position', size=24)
plt.xlabel('Vertical Release Position', size=18)
plt.ylabel('Frequency', size=18);

#------------------------------------------------------------------------------------------------------------------------------------------------------------


# regression plot using seaborn on vertical release and velo (sliders)
fig = plt.figure(figsize=(10, 7))
sns.regplot(x=clase_sliders.release_pos_z, y=clase_sliders.release_speed, color="r", marker='+')
#title, and labels.
plt.title('Emmannuel Clase (2022 Sliders) Relationship between Vertical Release Height and Velocity ', size=24)
plt.xlabel('Vertical Release Height (ft)', size=18)
plt.ylabel('Velocity (mph)', size=18)


# regression plot using seaborn on horizontal release and velo (sliders)

fig = plt.figure(figsize=(10, 7))
sns.regplot(x=clase_sliders.release_pos_x, y=clase_sliders.release_speed, color='b', marker='+')
plt.title('Emmannuel Clase (2022 Sliders) Relationship between Horizontal Release Position and Velocity ', size=24)
plt.xlabel('Horizontal Release Position (ft)', size=18)
plt.ylabel('Velocity (mph)', size=18)

#------------------------------------------------------------------------------------------------------------------------------------------------------------


# regression plot using seaborn on horizontal release and velo (FC)

fig = plt.figure(figsize=(10, 7))
sns.regplot(x=clase_cutters.release_pos_x, y=clase_cutters.release_speed, color="r", marker='+')
#title, and labels.
plt.title('Emmannuel Clase (2022 Cutters) Relationship between Vertical Release Height and Velocity ', size=18)
plt.xlabel('Vertical Release Height (ft)', size=18)
plt.ylabel('Velocity (mph)', size=18)


# regression plot using seaborn on vertical release and velo (FC)

fig = plt.figure(figsize=(10, 7))
sns.regplot(x=clase_cutters.release_pos_z, y=clase_cutters.release_speed, color="r", marker='+')
#title, and labels.
plt.title('Emmannuel Clase (2022 Cutters) Relationship between Vertical Release Height and Velocity ', size=18)
plt.xlabel('Vertical Release Height (ft)', size=18)
plt.ylabel('Velocity (mph)', size=18)

#------------------------------------------------------------------------------------------------------------------------------------------------------------


#create new df where the horizontal release on cutters and sliders >= -1.25
clase_cutters_new_rel = clase_cutters.loc[(clase_cutters['release_pos_x'] >= -1.25)]
clase_sliders_new_rel = clase_sliders.loc[(clase_sliders['release_pos_x'] >= -1.25)]


# regression plot using seaborn on horizontal release >+ -1.25 and velo (FC)

fig = plt.figure(figsize=(10, 7))
sns.regplot(x=clase_cutters_new_rel.release_pos_x, y=clase_cutters_new_rel.release_speed, color="b", marker='+')
#title, and labels.
plt.title('Emmannuel Clase (2022 Cutters) Relationship between Horizontal Release Position and Velocity ', size=18)
plt.xlabel('Horizontal Release Position (ft)', size=18)
plt.ylabel('Velocity (mph)', size=18)


# regression plot using seaborn on horizontal release >+ -1.25 and velo (SL)

fig = plt.figure(figsize=(10, 7))
sns.regplot(x=clase_sliders_new_rel.release_pos_x, y=clase_sliders_new_rel.release_speed, color="b", marker='+')
#title, and labels.
plt.title('Emmannuel Clase (2022 Sliders) Relationship between Horizontal Release Position and Velocity ', size=18)
plt.xlabel('Horizontal Release Position (ft)', size=18)
plt.ylabel('Velocity (mph)', size=18)

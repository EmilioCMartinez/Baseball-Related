#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:12:49 2021
@author: EmilioMartinez
"""
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pybaseball as pyb
from pybaseball import statcast
from pybaseball import playerid_lookup
from pybaseball.plotting import plot_bb_profile, plot_stadium
from pybaseball import statcast_batter,statcast_pitcher,spraychart,team_pitching,team_pitching_bref,pitching_stats,batting_stats


#import castro playerid
player = playerid_lookup('Castro','Miguel')
#get 2020 castro data
castro = statcast_pitcher('2020-01-01','2020-12-31',612434)

#make data only contain sliders (boolean)
new1 = castro['pitch_type'].isin(['SL'])  

#change data frame back to original with only sliders
data_castro = castro[new1]

#create variables wanted to see, this shows sensitivity of horizontal movement to spin rate and velo
x = data_castro['release_speed']

y = data_castro['release_spin_rate']
z = data_castro['pfx_x']*12

#plot figures
fig = plt.figure()
ax = fig.gca(projection='3d')

trisurf1 = ax.plot_trisurf(x, y, z, linewidth=0.2,cmap = 'jet', antialiased=True)
ax.set_xlabel('Velocity')
ax.set_ylabel('Spin Rate') 
ax.set_zlabel('Horizontal Movement (in.)')
fig.colorbar(trisurf1, ax = ax, shrink = .5, aspect = 5,label = 'Horizontal Movement') 
plt.title('Miguel Castro 2020 SL Horizontal Movement Sensitivity to Spin Rate and Velocity')
plt.show()


#import castillo playerid
player = playerid_lookup('Castillo','Luis')
#get 2020 castillo data
castillo = statcast_pitcher('2020-01-01','2020-12-31',622491)

#make data only contain sliders (boolean)
new2 = castillo['pitch_type'].isin(['SL'])  

#change data frame back to original with only sliders
data_castillo = castillo[new2]

#create variables wanted to see, this shows sensitivity of horizontal movement to spin rate and velo
x = data_castillo['release_speed']

y = data_castillo['release_spin_rate']
z = data_castillo['pfx_x']*12

#plot figures
fig = plt.figure()
ax = fig.gca(projection='3d')

trisurf= ax.plot_trisurf(x, y, z, linewidth=0.2,cmap = 'jet', antialiased=True)
ax.set_xlabel('Velocity')
ax.set_ylabel('Spin Rate') 
ax.set_zlabel('Horizontal Movement (in.)')
fig.colorbar(trisurf, ax = ax, shrink = .5, aspect = 5,label = 'Horizontal Movement') 
plt.title('Luis Castillo 2020 SL Horizontal Movement Sensitivity to Spin Rate and Velocity')
plt.show()

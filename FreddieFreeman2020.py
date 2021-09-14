#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:03:29 2021
@author: EmilioMartinez
"""


import pybaseball as pyb
from pybaseball import statcast
from pybaseball import playerid_lookup
from pybaseball.plotting import plot_bb_profile, plot_stadium
from pybaseball import statcast_batter,statcast_pitcher,spraychart,team_pitching,team_pitching_bref,pitching_stats,batting_stats
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd 
import numpy as np 

#Get Freddie Freeman player ID
player = playerid_lookup('Freeman','Freddie')

#Get hitting statcat data from 2020 season for freddie
freeman = statcast_batter('2020-01-01','2020-12-31',518692) 

#Create new column , hard_hit, which determines if a ball was hit >= 95mph EV
freeman.loc[(freeman['launch_speed'] >= 95) , 'hard_hit'] = 'yes'  
freeman.loc[(freeman['launch_speed'] < 95) , 'hard_hit'] = 'no'   

#Create a new column, sweet_spot, whcih determines if a ball was hit between 8 and 32 deegrees LA
freeman.loc[(freeman['launch_angle'] >= 8) & (freeman['launch_angle'] <= 32),'sweet_spot'] = 'yes'
freeman.loc[(freeman['launch_angle'] < 8) | (freeman['launch_angle'] > 32),'sweet_spot'] = 'no'

#Create new freddie data frame to manipulate so that the old one is available for other analysis if you choose, this keeps all balls >=95 EV and between 8 and 32 degrees LA
freeman_new = freeman.loc[(freeman['launch_speed'] >= 95) & (freeman['launch_angle'] >=8) & (freeman['launch_angle'] <= 32)]



#Create figure to plot data points
fig,ax = plt.subplots(1)

#points that are all bbe
plt.scatter(x=freeman['launch_speed'],
                             y=freeman['launch_angle'],facecolors='none', edgecolors='grey')
#BBe that are >+ 95EV and 80 to 32 degree LA
plt.scatter(x=freeman_new['launch_speed'],
                             y=freeman_new['launch_angle'],
                             color = 'r',alpha=1,edgecolors='k',label = 'Qualified Sweet Spot & Hard Hit')
#Create rectangle to show 8 to 32 degree LA
rect = patches.Rectangle((0,8),125,24,linewidth=2,facecolor='gold',alpha = .3,label = '8\xb0 to 32\xb0 LA ')
plt.vlines(95, -90, 90, color = 'k')
# Add the patch to the Axes
ax.add_patch(rect)

plt.xlim(0, 125) 
plt.ylim(-90, 90) 
plt.xlabel('Exit Velocity')
plt.ylabel('Launch Angle')
plt.title('Freddie Freeman 2020 Sweet Spot and Hard Hit')
plt.legend(loc='upper left', frameon=False)
plt.show()



#function to plot stadium from pybaseball plotting csv
stadium = pd.read_csv('https://raw.githubusercontent.com/jldbc/pybaseball/master/pybaseball/data/mlbstadiums.csv')
stadium['y'] = stadium['y'] * -1
stadium = stadium.loc[:,'team':]
def plot_stadium(team, color):
    team_df = stadium[stadium['team'] == team.lower()]
    for i in stadium['segment'].unique():
        data = team_df[team_df['segment'] == i]
        plt.plot(data['x'],data['y'], linestyle = '-', color = color) 
    #plt.suptitle(team.capitalize(), y=.975, fontsize=15)
    plt.title(team_df['location'].any(), fontsize=8)
    plt.axis('off')

#Create variable to lower size so it looks better on plot
z = freeman_new['hit_distance_sc']/3.5

plot_stadium('braves','black') 
plt.scatter(x=freeman_new['hc_x'], y=freeman_new['hc_y']*-1,c=freeman_new['launch_angle'], s=z, cmap=plt.cm.YlOrRd)
cb = plt.colorbar()
cb.set_label('Launch Angle')
plt.suptitle('Freddie Freeman 2020 Hard Hit and Sweet Spot Spray Chart', y=.975, fontsize=15)
plt.title('Overlaid at Truist Park')
plt.show()

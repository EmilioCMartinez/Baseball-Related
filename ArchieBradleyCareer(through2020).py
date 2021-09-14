#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:19:46 2021
@author: EmilioMartinez
"""
from pybaseball.plotting import plot_bb_profile, plot_stadium
import pybaseball as pyb
from pybaseball import statcast
from pybaseball import statcast_batter,statcast_pitcher,spraychart,team_pitching,team_pitching_bref,pitching_stats,batting_stats
import pandas as pd 
import matplotlib.pyplot as plt
from pybaseball import playerid_lookup
import numpy as np
 

#get playeer id for archie
player=playerid_lookup('Bradley','Archie')
#get his career stats
data_archie = statcast_pitcher('2015-01-01', '2020-12-31', 605151)

#label hit or out by event
data_archie.loc[(data_archie['events'] == 'single') | (data_archie['events'] == 'double')| (data_archie['events'] == 'triple')| (data_archie['events'] == 'home_run'), 'hit_out'] = 'hit'  
data_archie.loc[(data_archie['events'] != 'single') & (data_archie['events'] != 'double') & (data_archie['events'] != 'triple') & (data_archie['events'] != 'home_run'), 'hit_out'] = 'out' 

#Hexbin using BBE coordinates, change color basedo n what metric wants to be shown
plt.hexbin(data_archie['hc_x'], data_archie['hc_y']*-1, C=data_archie['launch_speed']>50 ,cmap=plt.cm.YlOrRd, gridsize = 20)
cb = plt.colorbar()
cb.set_label('Exit Velo')
#plt.xlabel('Exit Velocity')
#plt.ylabel('Launch Angle') 
plt.title('Archie Bradley Career Hits Allowed Density')

plt.show() 

#Create a function using the stadium csv ile from pybaseball. This will plot outlines of all stadiums
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

#Overlay archie hexbin of hits with Citizens bank park
plt.hexbin(data_archie['hc_x'], data_archie['hc_y']*-1, C=data_archie['hit_out']=='hit',cmap=plt.cm.YlOrRd, gridsize = 25)
plot_stadium('phillies','black') 
cb = plt.colorbar()
cb.set_label('Hit Probablity') 
plt.suptitle('Archie Bradley Career Hit Allowance', y=.975, fontsize=15)
plt.title('Overlaid at Citizens Bank Park')
plt.show()

#Overlay archie hexbin of EV with Citizens bank park
plot_stadium('phillies','black')
plt.hexbin(data_archie['hc_x'], data_archie['hc_y']*-1, C=data_archie['launch_speed'],cmap=plt.cm.Spectral_r, gridsize = 25)
cb = plt.colorbar()
cb.set_label('Exit Velocity') 
plt.suptitle('Archie Bradley Career BBE by Exit Velocity', y=.975, fontsize=15)
plt.title('Overlaid at Citizens Bank Park')
plt.show()

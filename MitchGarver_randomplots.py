#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:18:45 2020
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
import matplotlib.pyplot as plt
import seaborn as sns
import ptitprince as pt 



player=playerid_lookup('Garver','Mitch')

data_mitch = statcast_batter('2017-01-01', '2020-12-31', 641598)



data_mitch.loc[(data_mitch['events'] == 'single') | (data_mitch['events'] == 'double')| (data_mitch['events'] == 'triple')| (data_mitch['events'] == 'home_run'), 'hit_out'] = 'hit'  
data_mitch.loc[(data_mitch['events'] != 'single') & (data_mitch['events'] != 'double') & (data_mitch['events'] != 'triple') & (data_mitch['events'] != 'home_run'), 'hit_out'] = 'out' 

#--------------------------------------------

plt.hexbin(data_mitch['launch_speed'], data_mitch['launch_angle'], C=data_mitch['hit_out']=='hit',cmap=plt.cm.YlOrRd, gridsize = 55)
cb = plt.colorbar()
cb.set_label('Hit Probablity')
plt.xlabel('Exit Velocity')
plt.ylabel('Launch Angle') 
plt.title('Mitch Garver Career Hit Probability by EV & LA')
plt.xlim(0,130)
plt.show()
#--------------------------------------------
plt.hexbin(data_mitch['hc_x'], data_mitch['hc_y']*-1, C=data_mitch['hit_out']=='hit',cmap=plt.cm.YlOrRd, gridsize = 70)
cb = plt.colorbar()
cb.set_label('Hit Probablity')
plt.xlabel('Exit Velocity')
plt.ylabel('Launch Angle') 
plt.title('Mitch Garver Career Hit Density')

plt.show()
#--------------------------------------------

plot_bb_profile(data_mitch, parameter="launch_angle")
plt.legend()
plt.show()
#--------------------------------------------
ax1=sns.boxplot(x='pitch_type', y='launch_speed', hue='p_throws', data= data_mitch, palette="Set1")
ax1.set_title('Mitch Garver EV by Pitch Type')
ax1.set(ylim=(0,120))
ax1.set_ylabel('Evit Velocity (mph)')
ax1.set_xlabel('Pitch Type')
plt.legend(bbox_to_anchor=(1, 0.50),borderaxespad=0)
plt.show()
#--------------------------------------------
rmitch = data_mitch[data_mitch['p_throws']=='R']
lmitch = data_mitch[data_mitch['p_throws']=='L']


ax = sns.boxplot(x = 'pitch_type', y = 'launch_speed', data = rmitch) 
ax.set(ylim=(0,120))
ax.set_title('Mitch Garver EV by Pitch Type (Righty)')
ax.set_ylabel('Evit Velocity (mph)')
ax.set_xlabel('Pitch Type')
plt.show()
#--------------------------------------------
ax2 = sns.boxplot(x = 'pitch_type', y = 'launch_speed', data = lmitch) 
ax2.set(ylim=(0,120))
ax2.set_title('Mitch Garver EV by Pitch Type (Lefty)')
ax2.set_ylabel('Evit Velocity (mph)')
ax2.set_xlabel('Pitch Type')
plt.show()
#--------------------------------------------



new=data_mitch.copy()

new.drop(new.loc[new['events']=='field_error'].index, inplace=True)
new.drop(new.loc[new['events']=='field_out'].index, inplace=True)
new.drop(new.loc[new['events']=='fielders_choice_out'].index, inplace=True)
new.drop(new.loc[new['events']=='force_out'].index, inplace=True)
new.drop(new.loc[new['events']=='grounded_into_double_play'].index, inplace=True)
new.drop(new.loc[new['events']=='sac_fly'].index, inplace=True)
new.drop(new.loc[new['events']=='sac_bunt'].index, inplace=True)

spraychart(new,'twins', title='Mitch Garver', colorby='events')

#--------------------------------------------
stadium = pd.read_csv('https://raw.githubusercontent.com/jldbc/pybaseball/master/pybaseball/data/mlbstadiums.csv')
stadium['y'] = stadium['y'] * -1
stadium = stadium.loc[:,'team':]
def plot_stadium(team, color):
    team_df = stadium[stadium['team'] == team.lower()]
    for i in stadium['segment'].unique():
        data = team_df[team_df['segment'] == i]
        plt.plot(data['x'],data['y'], linestyle = '-', color = color) 
    plt.suptitle(team.capitalize(), y=.975, fontsize=15)
    plt.title(team_df['location'].any(), fontsize=8)
    plt.axis('off')

plot_stadium('twins','black') 
plt.hexbin(data_mitch['hc_x'], data_mitch['hc_y']*-1, C=data_mitch['hit_out']=='hit',cmap=plt.cm.YlOrRd, gridsize = 70)
cb = plt.colorbar()
cb.set_label('Hit Probablity')
plt.xlabel('Exit Velocity')
plt.ylabel('Launch Angle') 
plt.title('Mitch Garver Career Hit Density')
#--------------------------------------------

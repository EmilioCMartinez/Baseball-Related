#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:35:33 2021
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



#lookup lindoor id
player=playerid_lookup('Lindor','Francisco')

#get career batting data for lindor
data_lindor = statcast_batter('2015-01-01', '2020-12-31', 596019)

#describe whether the batted ball event was a hit or out 

data_lindor.loc[(data_lindor['events'] == 'single') | (data_lindor['events'] == 'double')| (data_lindor['events'] == 'triple')| (data_lindor['events'] == 'home_run'), 'hit_out'] = 'hit'  
data_lindor.loc[(data_lindor['events'] != 'single') & (data_lindor['events'] != 'double') & (data_lindor['events'] != 'triple') & (data_lindor['events'] != 'home_run'), 'hit_out'] = 'out' 




#create new dataset removing all events that were not a hit or sac fly

new=data_lindor.copy()

new.drop(new.loc[new['events']=='field_error'].index, inplace=True)
new.drop(new.loc[new['events']=='field_out'].index, inplace=True)
new.drop(new.loc[new['events']=='fielders_choice_out'].index, inplace=True)
new.drop(new.loc[new['events']=='force_out'].index, inplace=True)
new.drop(new.loc[new['events']=='grounded_into_double_play'].index, inplace=True)
new.drop(new.loc[new['events']=='sac_bunt'].index, inplace=True)
new.drop(new.loc[new['events']=='walk'].index, inplace=True)
new.drop(new.loc[new['events']=='strikeout'].index, inplace=True)
new.drop(new.loc[new['events']=='caught_stealing_2b'].index, inplace=True) 
new.drop(new.loc[new['events']=='hit_by_pitch'].index, inplace=True) 
new.drop(new.loc[new['events']=='pickoff_caught_stealing_2b'].index, inplace=True) 
new.drop(new.loc[new['events']=='strikeout_double_play'].index, inplace=True) 
new.drop(new.loc[new['events']=='double_play'].index, inplace=True) 
new.drop(new.loc[new['events']=='fielders_choice'].index, inplace=True) 



#create new dataset that only has balls in play that were not a hit or sac fly, only hit at CLEVELAND'S field, removing all nan events
home_lindor = new.loc[new['home_team'] == 'CLE']
home_lindor = home_lindor[home_lindor['events'].notna()]


#read in stadium csv from pybaseball
stadium = pd.read_csv('https://raw.githubusercontent.com/jldbc/pybaseball/master/pybaseball/data/mlbstadiums.csv')
#create new y variable since it needs to be a negative value in order to be plotted

stadium['y'] = stadium['y'] * -1
stadium = stadium.loc[:,'team':]

#function to plot outline of a certain stadium and the color of the outline 
def plot_stadium(team, color):
    team_df = stadium[stadium['team'] == team.lower()]
    for i in stadium['segment'].unique():
        data = team_df[team_df['segment'] == i]
        plt.plot(data['x'],data['y'], linestyle = '-', color = color) 
    #plt.suptitle(team.capitalize(), y=.975, fontsize=15)
    #plt.title(team_df['location'].any(), fontsize=8)
    plt.axis('off')

#create dataframes to plot to set individual labels for the plot 
single = home_lindor.loc[home_lindor['events'] == 'single']
double = home_lindor.loc[home_lindor['events'] == 'double']
triple = home_lindor.loc[home_lindor['events'] == 'triple']
hr = home_lindor.loc[home_lindor['events'] == 'home_run']
sf = home_lindor.loc[home_lindor['events'] == 'sac_fly']


plot_stadium('indians','black') 
plot_stadium('mets','orange') 
plt.scatter(single['hc_x'],single['hc_y']*-1,color='gainsboro',label = 'Single')
plt.scatter(double['hc_x'],double['hc_y']*-1,color='royalblue',label = 'Double')
plt.scatter(triple['hc_x'],triple['hc_y']*-1,color='firebrick',label = 'Triple')
plt.scatter(hr['hc_x'],hr['hc_y']*-1,color='red',label = 'Home Run')
plt.scatter(sf['hc_x'],sf['hc_y']*-1,color='dimgrey',label = 'Sac Fly')

plt.legend(title = 'Batted Ball Type',loc=(0, -0.1))
plt.title('Lindor Career at Progressive Field (black) overlayed with Citi Field (orange) ',fontweight="bold")

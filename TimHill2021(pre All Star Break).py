import pybaseball as pyb
from pybaseball import statcast
from pybaseball import playerid_lookup
from pybaseball import statcast_batter,statcast_pitcher
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd 
import numpy as np 

player = playerid_lookup('Hill', 'Tim')

#Get hitting statcat data from 2021 season for hill
hill = statcast_pitcher('2021-01-01','2021-12-31', 657612) 



#label hit or out by event
hill.loc[(hill['events'] == 'single') | (hill['events'] == 'double')| (hill['events'] == 'triple')| (hill['events'] == 'home_run'), 'hit_out'] = 'hit'  
hill.loc[(hill['events'] != 'single') & (hill['events'] != 'double') & (hill['events'] != 'triple') & (hill['events'] != 'home_run'), 'hit_out'] = 'out' 


plt.hexbin(hill['plate_x'], hill['plate_z'], C=hill['hit_out']=='hit',cmap=plt.cm.YlOrRd, gridsize = 25)



def plot_pitches(plotdf):
    strikezone = plt.Rectangle((-.95,1.6), 1.65, 1.8, color='black', fill=False,alpha = 1)
    heart = plt.Rectangle((-.55,2.0125), 0.825, 0.9, color='red', fill=False,alpha = 1)
    groups = plotdf.groupby("pitch_type")
    for name, group in groups:
        plt.plot(group["plate_x"], group["plate_z"], marker="o", linestyle="", label=name, alpha=.55) 

    plt.ylim((0,5))
    plt.xlim((-3,3))
    plt.gca().add_patch(strikezone)
    plt.gca().add_patch(heart)
    plt.legend(bbox_to_anchor=(1,1), loc='upper right', ncol=1) 
    plt.title('Tim Hill 2021 Pitches (K-zone)')




def plotstrikezone(df):
    
    strikezone = plt.Rectangle((-.95,1.6), 1.65, 1.8, color='black', fill=False,alpha = .25)
    heart = plt.Rectangle((-.55,2.0125), 0.825, 0.9, color='red', fill=False,alpha = .25)
    plt.ylim((0,5))
    plt.xlim((-3,3))
    plt.gca().add_patch(strikezone)
    plt.gca().add_patch(heart)



plt.hexbin(hill['plate_x'], hill['plate_z'], C=hill['hit_out']=='hit',cmap=plt.cm.YlOrRd, gridsize = 15) 
plt.title('Tim Hill 2021 Hit Density (K-zone)')
cb = plt.colorbar()
cb.set_label('Hit Density') 

#plotstrikezone(hill) 


#plot_pitches(hill)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 10:19:44 2020
@author: EmilioMartinez
"""
from pybaseball import statcast
from pybaseball import statcast_batter,statcast_pitcher,spraychart
import pandas as pd 
import matplotlib.pyplot as plt
from pybaseball import playerid_lookup
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

player = playerid_lookup('Ottavino','Adam')
dataBauer = statcast_pitcher('2019-03-01', '2019-12-31', 545333)
dataOttavino = statcast_pitcher('2019-03-01', '2019-12-31', 493603) 
Ottavino = dataOttavino.drop(dataOttavino.index[588:616])
Bauer = dataBauer[~(dataBauer['release_speed'] <= 60)] 

Bauer.pitch_type.unique()
Ottavino.pitch_type.unique()

def plot_ecdf(data,title = "ECDF Plot", xlabel = 'Data Values', ylabel = 'Percentage'):
    
    """ 
    Function to plot ecdf taking a column of data as input.
    """
    xaxis = np.sort(data)
    yaxis = np.arange(1, len(data)+1)/len(data)
    plt.plot(xaxis,yaxis,linestyle='none',marker='.')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.margins(0.02) 
    

pitchesBauer = Bauer.pitch_type.unique()

sns.relplot(x='release_spin_rate', y='release_extension', hue='pitch_type',#size='spinrate'
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=Bauer)


for pitch in pitchesBauer:
    plot_ecdf(Bauer['release_extension'][Bauer.pitch_type == pitch])
plt.legend(pitchesBauer)
plt.show()


plot_ecdf(Bauer['release_extension'][Bauer.pitch_type == 'FF'],title='Bauer Extension % by Pitch',xlabel = 'Extension',ylabel='Percentage')
plot_ecdf(Bauer['release_extension'][Bauer.pitch_type == 'SL'],title='Bauer Extension % by Pitch',xlabel = 'Extension',ylabel='Percentage')
plot_ecdf(Bauer['release_extension'][Bauer.pitch_type == 'KC'],title='Bauer Extension % by Pitch',xlabel = 'Extension',ylabel='Percentage')
plot_ecdf(Bauer['release_extension'][Bauer.pitch_type == 'FT'],title='Bauer Extension % by Pitch',xlabel = 'Extension',ylabel='Percentage')
plt.legend(pitchesBauer[[0,5,2,3]])
plt.show()


plot_ecdf(Bauer['release_pos_z'][Bauer.pitch_type == 'FF'],title='Bauer Vertical Release % by Pitch',xlabel = 'Vertical Release',ylabel='Percentage')
plot_ecdf(Bauer['release_pos_z'][Bauer.pitch_type == 'SL'],title='Bauer Vertical Release % by Pitch',xlabel = 'Vertical Release',ylabel='Percentage')
plot_ecdf(Bauer['release_pos_z'][Bauer.pitch_type == 'KC'],title='Bauer Vertical Release % by Pitch',xlabel = 'Vertical Release',ylabel='Percentage')
plot_ecdf(Bauer['release_pos_z'][Bauer.pitch_type == 'FT'],title='Bauer Vertical Release % by Pitch',xlabel = 'Vertical Release',ylabel='Percentage')
plt.legend(pitchesBauer[[0,5,2,3]])
plt.show()


plot_ecdf(Bauer['release_pos_x'][Bauer.pitch_type == 'FF'],title='Bauer Horizontal Release % by Pitch',xlabel = 'Horizonal Release',ylabel='Percentage')
plot_ecdf(Bauer['release_pos_x'][Bauer.pitch_type == 'SL'],title='Bauer Horizontal Release % by Pitch',xlabel = 'Horizonal Release',ylabel='Percentage')
plot_ecdf(Bauer['release_pos_x'][Bauer.pitch_type == 'KC'],title='Bauer Horizontal Release % by Pitch',xlabel = 'Horizonal Release',ylabel='Percentage')
plot_ecdf(Bauer['release_pos_x'][Bauer.pitch_type == 'FT'],title='Bauer Horizontal Release % by Pitch',xlabel = 'Horizonal Release',ylabel='Percentage')
plt.legend(pitchesBauer[[0,5,2,3]])
plt.gca().invert_xaxis()
plt.show()


pitchesOttavino= Ottavino.pitch_type.unique()


sns.relplot(x='release_spin_rate', y='release_extension', hue='pitch_type', #size='release_spin_rate',
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=Ottavino)


for pitch in pitchesOttavino:
    plot_ecdf(Ottavino['release_extension'][Ottavino.pitch_type == pitch],title = 'Ottavino Extension % by Pitch',xlabel = 'Extension')
plt.legend(pitchesOttavino)
plt.show()


plot_ecdf(Ottavino['release_extension'][Ottavino.pitch_type == 'FT'],title='Ottavino Extension % by Pitch',xlabel = 'Extension',ylabel='Percentage')
plot_ecdf(Ottavino['release_extension'][Ottavino.pitch_type == 'SL'],title='Ottavino Extension % by Pitch',xlabel = 'Extension',ylabel='Percentage')
plt.legend(pitchesOttavino[[0,2]])
plt.show()


plot_ecdf(Ottavino['release_pos_z'][Ottavino.pitch_type == 'FT'],title='Ottavino Vertical Release % by Pitch',xlabel = 'Vertical Release',ylabel='Percentage')
plot_ecdf(Ottavino['release_pos_z'][Ottavino.pitch_type == 'SL'],title='Ottavino Vertical Release % by Pitch',xlabel = 'Vertical Release',ylabel='Percentage')
plt.legend(pitchesOttavino[[0,2]])
plt.show()


plot_ecdf(Ottavino['release_pos_x'][Ottavino.pitch_type == 'FT'],title='Ottavino Horizontal Release % by Pitch',xlabel = 'Horizontal Release',ylabel='Percentage')
plot_ecdf(Ottavino['release_pos_x'][Ottavino.pitch_type == 'SL'],title='Ottavino Horizontal Release % by Pitch',xlabel = 'Horizontal Release',ylabel='Percentage')
plt.legend(pitchesOttavino[[0,2]])
plt.gca().invert_xaxis()
plt.show()

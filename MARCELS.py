#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 19:00:47 2021

@author: EmilioMartinez
"""


# inspired by: https://www.pitcherlist.com/pitcher-list-data-camp-intro-to-player-projections-with-r/   

import pandas as pd 
import pybaseball as pyb 
import numpy as np  


#fangraphs data from 2017-2021 

fg_2021 = pyb.batting_stats(2021,qual = 0)
fg_2020 = pyb.batting_stats(2020,qual = 0)
fg_2019 = pyb.batting_stats(2019,qual = 0)


#fg_2018 = pyb.batting_stats(2018,qual = 0).loc[fg_2018['PA'] > 300] 
#fg_2017 = pyb.batting_stats(2017,qual = 0).loc[fg_2017['PA'] > 300]

#Create new data frames ony consising of 4 columns that are of interest 

stat_2021= fg_2021[['Name','IDfg','PA','HR']]
stat_2020= fg_2020[['Name','IDfg','PA','HR']]
stat_2019= fg_2019[['Name','IDfg','PA','HR']]


#stat_2018= fg_2018[['Name','IDfg','PA','HR']]
#stat_2017= fg_2017[['Name','IDfg','PA','HR']]


stat_2021 = stat_2021.rename(columns={'HR': 'HR_1', 'PA': 'PA_1'})
stat_2020 = stat_2020.rename(columns={'HR': 'HR_2', 'PA': 'PA_2'})
stat_2019 = stat_2019.rename(columns={'HR': 'HR_3', 'PA': 'PA_3'}) 

#stat_full is the three data sets combined (19,20,21)
stat = pd.merge(stat_2021, stat_2020,on=['Name','IDfg'])  
stat_full = pd.merge(stat,stat_2019,on=['Name','IDfg']).fillna(0) #fillna replace all Nan values with zeroes


#see what the data looks like with PA_1 >30 ab  
stat_full.loc[stat_full['PA_1'] > 300].head() 

#  "Weight each season on the 3/4/5 (3 representing 2019, 4 from 2020, and 5 from 2021)." -pitcherlist article

stat_full['HR_tot'] = stat_full['HR_1'] * 5  + stat_full['HR_2'] * 4 +stat_full['HR_3'] * 3 
stat_full['PA_tot'] = stat_full['PA_1'] * 5  + stat_full['PA_2'] * 4 +stat_full['PA_3'] * 3  



avg_2021 = sum(stat_full['HR_1'])/ sum(stat_full['PA_1'])
avg_2020 = sum(stat_full['HR_2']) / sum(stat_full['PA_2'])
avg_2019 = sum(stat_full['HR_3']) / sum(stat_full['PA_3'])   

#"Determine the league average HR/PA for each season and multiply by the number of plate appearances 
#the player had in each season, and then sum them using the 3/4/5 scale. We then prorate it to 1200 PA, as Tom outlines."
stat_full['reg'] = (5 * stat_full['PA_1'] * avg_2021)  +  (4 * stat_full['PA_2'] * avg_2020 )+ (3 * stat_full['PA_3'] * avg_2019 * 1200/ stat_full['PA_tot']) 


#"Determine the projected plate appearances using Tom’s scale. Then use the information we have (HR/PA) to project home runs."
stat_full['HR_Raw'] = stat_full['HR_tot'] + stat_full['reg']
stat_full['PA_Raw'] = stat_full['PA_tot'] + 1200
stat_full['HR_PA'] = stat_full['HR_Raw'] / stat_full['PA_Raw'] 

stat_full['PA_proj'] = 0.5 * stat_full['PA_1'] + 0.1 * stat_full['PA_2'] + 200 
stat_full['HR_proj'] = stat_full['HR_PA'] * stat_full['PA_proj']  



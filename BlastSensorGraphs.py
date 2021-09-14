"""
@author: EmilioMartinez
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


#bat speed = 7     |
#Attack Angle = 10 | >>> column assignments for each metric
#Vert angle = 13   |
#Time to Cont = 15 |


#IMPORT TEE VALUES
tee = pd.read_csv('/Users/EmilioMartinez/Desktop/tee.csv',usecols=[7,9,10,15],skiprows=7)
tee.dropna(inplace = True)#Drop all values in columns that say 'NaN' 
tee.columns = ['BatSpeedTee','PlaneEffTee','AttackAngleTee','TimeToContactTee']
#print(tee)

#IMPORT LIVE VALUES
live = pd.read_csv('/Users/EmilioMartinez/Desktop/live:machine.csv',usecols=[7,9,10,15],skiprows=7)
live.dropna(inplace = True)#Drop all values in columns that say 'NaN' 
live.columns = ['BatSpeedLive','PlaneEffLive','AttackAngleLive','TimeToContactLive']
#print(live)

#Merge the two dataframes
metrics = pd.concat([tee,live], axis = 1)

#Get Avg values for AA on tee and live
AVG_teeAA = metrics["AttackAngleTee"].mean()
AVG_teeAA=round(AVG_teeAA, 1)
AVG_liveAA = metrics["AttackAngleLive"].mean()
AVG_liveAA=round(AVG_liveAA, 1)


#Create density plot with text to show average attack angles on both tee and live


p1=sns.kdeplot(metrics['AttackAngleTee'], shade=True, color="r")
p1=sns.kdeplot(metrics['AttackAngleLive'], shade=True, color="b")
p1.set_title('Attack Angle (Tee vs Live)')
p1.set_ylabel('Fequency')
p1.set_xlabel('Attack Angle (deg)')
plt.text(-8.5, 0.12, 'Average AA (tee): {}'.format(AVG_teeAA),fontsize=9,fontweight='bold')
plt.text(20, 0.05, 'Average AA (live): {}'.format(AVG_liveAA),fontsize=9,fontweight='bold')

'''
p2 = sns.pairplot(tee, kind = 'reg')
p2.set_title('Tee Correlation')
sns.plt.show() 
'''
p3 =sns.pairplot(live, kind = 'reg')
p3.set_title('Live Correlations')
sns.plt.show() 

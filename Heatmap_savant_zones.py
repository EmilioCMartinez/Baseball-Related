#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 10:22:10 2022

@author: emiliomartinez
"""

# importing the modules
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle





fig, ax = plt.subplots(figsize=(10,10))

data = np.random.randint(low = 90,
                         high = 100,
                         size = (10, 10))

#print("The data to be plotted:\n")
#print(data) 
sn.heatmap(data = data,cmap = 'coolwarm') 
ax.vlines([5], 0, 2, colors='black',lw = 5)
ax.vlines([5], 8, 10, colors='black',lw = 5)
ax.hlines([5], 8, 10, colors='black',lw = 5)
ax.hlines([5], 0, 2, colors='black',lw = 5)



ax.add_patch(Rectangle((0, 0), 10, 10,
             edgecolor = 'black',fill=False,
             lw=7))

ax.add_patch(Rectangle((2, 6), 2, 2,
             edgecolor = 'black',fill=False,
             lw=5))
ax.add_patch(Rectangle((4, 6), 2, 2,
             edgecolor = 'black',fill=False,
             lw=5)) 
ax.add_patch(Rectangle((6, 6), 2, 2,
             edgecolor = 'black',fill=False,
             lw=5))


ax.add_patch(Rectangle((2, 4), 2, 2,
             edgecolor = 'black',fill=False,
             lw=5))
ax.add_patch(Rectangle((4, 4), 2, 2,
             edgecolor = 'black',fill=False,
             lw=5)) 
ax.add_patch(Rectangle((6, 4), 2, 2,
             edgecolor = 'black',fill=False,
             lw=5))

ax.add_patch(Rectangle((2, 2), 2, 2,
             edgecolor = 'black',fill=False,
             lw=5))
ax.add_patch(Rectangle((4, 2), 2, 2,
             edgecolor = 'black',fill=False,
             lw=5)) 
ax.add_patch(Rectangle((6, 2), 2, 2,
             edgecolor = 'black',fill=False,
             lw=5))

#--------------------------------------------------
#Create groups

#Zone 11 

ax.collections[0]._facecolors[0] = [0,0,1,1]
ax.collections[0]._facecolors[10] = [0,0,1,1]
ax.collections[0]._facecolors[20] = [0,0,1,1] 
ax.collections[0]._facecolors[30] = [0,0,1,1] 
ax.collections[0]._facecolors[40] = [0,0,1,1] 

ax.collections[0]._facecolors[1] = [0,0,1,1]
ax.collections[0]._facecolors[11] = [0,0,1,1]
ax.collections[0]._facecolors[21] = [0,0,1,1]
ax.collections[0]._facecolors[31] = [0,0,1,1]
ax.collections[0]._facecolors[41] = [0,0,1,1]

ax.collections[0]._facecolors[2] = [0,0,1,1]
ax.collections[0]._facecolors[12] = [0,0,1,1]
ax.collections[0]._facecolors[3] = [0,0,1,1] 
ax.collections[0]._facecolors[13] = [0,0,1,1] 
ax.collections[0]._facecolors[4] = [0,0,1,1] 
ax.collections[0]._facecolors[14] = [0,0,1,1] 


#Zone 12

ax.collections[0]._facecolors[8] = [0,0,1,1] 
ax.collections[0]._facecolors[18] = [0,0,1,1]
ax.collections[0]._facecolors[28] = [0,0,1,1] 
ax.collections[0]._facecolors[38] = [0,0,1,1] 
ax.collections[0]._facecolors[48] = [0,0,1,1]

ax.collections[0]._facecolors[9] = [0,0,1,1] 
ax.collections[0]._facecolors[19] = [0,0,1,1] 
ax.collections[0]._facecolors[29] = [0,0,1,1]
ax.collections[0]._facecolors[39] = [0,0,1,1]
ax.collections[0]._facecolors[49] = [0,0,1,1] 

ax.collections[0]._facecolors[5] = [0,0,1,1] 
ax.collections[0]._facecolors[15] = [0,0,1,1] 
ax.collections[0]._facecolors[6] = [0,0,1,1]
ax.collections[0]._facecolors[16] = [0,0,1,1] 
ax.collections[0]._facecolors[7] = [0,0,1,1]
ax.collections[0]._facecolors[17] = [0,0,1,1] 

#Zone 13 

ax.collections[0]._facecolors[50] = [0,0,1,1]
ax.collections[0]._facecolors[60] = [0,0,1,1] 
ax.collections[0]._facecolors[70] = [0,0,1,1] 
ax.collections[0]._facecolors[80] = [0,0,1,1] 
ax.collections[0]._facecolors[90] = [0,0,1,1] 

ax.collections[0]._facecolors[51] = [0,0,1,1] 
ax.collections[0]._facecolors[61] = [0,0,1,1] 
ax.collections[0]._facecolors[71] = [0,0,1,1] 
ax.collections[0]._facecolors[81] = [0,0,1,1] 
ax.collections[0]._facecolors[91] = [0,0,1,1] 

ax.collections[0]._facecolors[82] = [0,0,1,1] 
ax.collections[0]._facecolors[92] = [0,0,1,1] 
ax.collections[0]._facecolors[83] = [0,0,1,1] 
ax.collections[0]._facecolors[93] = [0,0,1,1] 
ax.collections[0]._facecolors[84] = [0,0,1,1] 
ax.collections[0]._facecolors[94] = [0,0,1,1] 

#Zone 14

ax.collections[0]._facecolors[58] = [0,0,1,1] 
ax.collections[0]._facecolors[68] = [0,0,1,1] 
ax.collections[0]._facecolors[78] = [0,0,1,1] 
ax.collections[0]._facecolors[88] = [0,0,1,1] 
ax.collections[0]._facecolors[98] = [0,0,1,1] 

ax.collections[0]._facecolors[59] = [0,0,1,1] 
ax.collections[0]._facecolors[69] = [0,0,1,1] 
ax.collections[0]._facecolors[79] = [0,0,1,1] 
ax.collections[0]._facecolors[89] = [0,0,1,1] 
ax.collections[0]._facecolors[99] = [0,0,1,1] 

ax.collections[0]._facecolors[85] = [0,0,1,1] 
ax.collections[0]._facecolors[95] = [0,0,1,1] 
ax.collections[0]._facecolors[86] = [0,0,1,1] 
ax.collections[0]._facecolors[96] = [0,0,1,1] 
ax.collections[0]._facecolors[87] = [0,0,1,1] 
ax.collections[0]._facecolors[97] = [0,0,1,1] 

#--------------------------------------------------------------------------


#Zone 1  123,456,789 

ax.collections[0]._facecolors[22] = [0,1,1,1] 
ax.collections[0]._facecolors[32] = [0,1,1,1] 
ax.collections[0]._facecolors[23] = [0,1,1,1]
ax.collections[0]._facecolors[33] = [0,1,1,1]  

#Zone 2  123,456,789 

ax.collections[0]._facecolors[24] = [0,1,1,1] 
ax.collections[0]._facecolors[34] = [0,1,1,1] 
ax.collections[0]._facecolors[25] = [0,1,1,1]
ax.collections[0]._facecolors[35] = [0,1,1,1]  

#Zone 3  123,456,789 

ax.collections[0]._facecolors[26] = [0,1,1,1] 
ax.collections[0]._facecolors[36] = [0,1,1,1] 
ax.collections[0]._facecolors[27] = [0,1,1,1]
ax.collections[0]._facecolors[37] = [0,1,1,1]  

#Zone 4  123,456,789 

ax.collections[0]._facecolors[42] = [0,1,1,1] 
ax.collections[0]._facecolors[52] = [0,1,1,1] 
ax.collections[0]._facecolors[43] = [0,1,1,1]
ax.collections[0]._facecolors[53] = [0,1,1,1]  

#Zone 5  123,456,789 

ax.collections[0]._facecolors[44] = [0,1,1,1] 
ax.collections[0]._facecolors[54] = [0,1,1,1] 
ax.collections[0]._facecolors[45] = [0,1,1,1]
ax.collections[0]._facecolors[55] = [0,1,1,1]  

#Zone 6  123,456,789 

ax.collections[0]._facecolors[46] = [0,1,1,1] 
ax.collections[0]._facecolors[56] = [0,1,1,1] 
ax.collections[0]._facecolors[47] = [0,1,1,1]
ax.collections[0]._facecolors[57] = [0,1,1,1]  

#Zone 7  123,456,789 

ax.collections[0]._facecolors[62] = [0,1,1,1] 
ax.collections[0]._facecolors[72] = [0,1,1,1] 
ax.collections[0]._facecolors[63] = [0,1,1,1]
ax.collections[0]._facecolors[73] = [0,1,1,1]  

#Zone 8  123,456,789 

ax.collections[0]._facecolors[64] = [0,1,1,1] 
ax.collections[0]._facecolors[74] = [0,1,1,1] 
ax.collections[0]._facecolors[65] = [0,1,1,1]
ax.collections[0]._facecolors[75] = [0,1,1,1]  

#Zone 9  123,456,789 

ax.collections[0]._facecolors[66] = [0,1,1,1] 
ax.collections[0]._facecolors[76] = [0,1,1,1] 
ax.collections[0]._facecolors[67] = [0,1,1,1]
ax.collections[0]._facecolors[77] = [0,1,1,1]  



plt.show()




import pandas as pd
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, read_csv
import matplotlib.ticker as ticker


plt.rcParams.update({'font.size': 32})

ax2 = plt.subplot(1, 1, 1)
#ax3 = plt.subplot2grid((8,8), (0, 5),rowspan=2)
#ax6 = plt.subplot2grid((8,8), (0, 6),rowspan=2)
#ax9 = plt.subplot2grid((8,8), (0, 7),rowspan=2)
#ax4 = plt.subplot2grid((8,8), (3, 5),rowspan=2)
#ax7 = plt.subplot2grid((8,8), (3, 6),rowspan=2)
#ax10 = plt.subplot2grid((8,8), (3, 7),rowspan=2)
#ax5 = plt.subplot2grid((8,8), (6, 5),rowspan=2)
#ax8 = plt.subplot2grid((8,8), (6, 6),rowspan=2)
#ax11 = plt.subplot2grid((8,8), (6, 7),rowspan=2)



x = np.array([0.02,0.04,0.06,0.08,0.10,0.12,0.14,0.16,0.18,0.20,0.22,0.24,0.26,0.28,0.30,0.32,0.34,0.36,0.38,0.40,0.42,0.44,0.46,0.48,0.50])

#base
y0 = np.array([23.306278, 23.470715, 23.639206, 23.876082, 24.208782, 24.638922, 25.474386, 27.909114, 108.767449, 368.012254, 576.419868, 725.558529, 864.219742, 960.319771, 1090.513419, 1203.552377, 1317.867079, 1449.492364, 1568.210950, 1719.882732, 1863.989605, 2012.851336, 2135.387639, 2367.574428, 2500])
#s
#y1=np.array([15.841985,15.925818,16.203575,16.261470,16.414911,16.519860,16.696600,16.971992,17.194129,17.515001,17.863588,18.521922,19.579682,23.716667,114.401260,303.273427,475.982530,671.896371,816.461257,1006.481345,1158.508684,1299.377256,1434.924839,1593.027771,1736.775331])
#y2=np.array([8.752877,8.873096,9.080524,9.202275,9.357376,9.492218,9.678108,9.894073,10.116519,10.379988,10.629412,10.998586,11.413593,12.045236,12.969750,15.585625,47.921177,219.487903,399.625183,573.624309,713.731005,861.584739,1015.271608,1155.351814,1307.480652])
#y3=np.array([5.246197,5.399103,5.616084,5.774054,5.958247,6.164364,6.389695,6.626899,6.903403,7.214344,7.511635,7.911074,8.349227,8.965828,9.800313,11.442370,22.021091,154.527040,319.364270,508.023240,660.956264,793.551966,964.592470,1080.141761,1244.314051])
#y4=np.array([3.536407,3.743194,3.983580,4.200913,4.479322,4.736035,5.086452,5.427490,5.783416,6.231383,6.675092,7.161476,7.744273,8.537415,9.535777,11.673363,29.380938,188.207640,334.644517,527.566642,686.416151,828.991033,970.555356,1136.934148,1296.693703])
#y5=np.array([3.193223,3.418270,3.689828,3.933919,4.240337,4.538822,4.914905,5.292504,5.683973,6.162574,6.623518,7.148901,7.757402,8.576372,9.663299,11.639939,34.330371,190.557146,340.556823,556.041505,682.808358,844.228688,992.130093,1125.984756,1284.217693])

#m
y6=np.array([13.839861, 14.510090, 15.122678, 15.796150, 16.534449, 17.364213, 18.424602, 19.995389, 28.342271, 216.030111, 453.096864, 627.842814, 770.115823, 870.655749, 993.410596, 1102.690295, 1207.120673, 1326.767572, 1436.673374, 1572.611576, 1721.338105, 1865.193754, 1996.316070, 2123.063061, 2227.496910])
y7=np.array([9.528883, 10.096080, 10.644789, 11.254491, 11.944166, 12.737437, 13.690482, 15.029598, 17.326814, 98.211579, 356.878682, 543.737291, 695.726945, 796.123420, 918.183870, 1027.964831, 1126.282453, 1241.491461, 1347.490295, 1473.659184, 1608.221322, 1757.215876, 1888.782918, 2018.331521, 2141.712733])
y8=np.array([5.531791, 6.088253, 6.726966, 7.451052, 8.274325, 9.205663, 10.315515, 11.744859, 13.892585, 55.377940, 312.473068, 516.506545, 665.421122, 779.441258, 892.187753, 1004.154494, 1097.581548, 1198.787831, 1315.729567, 1433.364558, 1556.994440, 1719.033111, 1844.649123, 1978.167862, 2094.554558])
#y9=np.array([3.432545,3.644715,3.903281,4.128557,4.410901,4.690064,5.053193,5.412761,5.770937,6.251254,6.675499,7.219559,7.812012,8.594203,9.695536,11.796995,33.985263,176.112580,349.579538,541.253947,692.518799,828.130612,989.986754,1128.713404,1288.924860])
#y10=np.array([3.193223,3.418270,3.689828,3.933919,4.240337,4.538822,4.914905,5.292504,5.683973,6.162574,6.623518,7.148901,7.757402,8.576372,9.663299,11.639939,34.330371,190.557146,340.556823,556.041505,682.808358,844.228688,992.130093,1125.984756,1284.217693])


#ideal1
#y11 = np.array([5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,1000])
y12 = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000])

ax2.plot(x, y0,'-',color='black',linewidth=4, label='BASE 1-c rtr',marker=u'x',markerfacecolor='white',markeredgecolor='black', markeredgewidth=2, markersize=15)

#ax2.plot(x, y1,'-',color='darkblue',linewidth=4, label='SMART (1)',marker=u'o',markerfacecolor='white',markeredgecolor='darkblue', markeredgewidth=2, markersize=15)
#ax2.plot(x, y2,'-',color='blue',linewidth=4, label='SMART (2)',marker=u's',markerfacecolor='white',markeredgecolor='blue', markeredgewidth=2, markersize=15)
#ax2.plot(x, y3,'-',color='royalblue',linewidth=4, label='SMART (4)',marker=u'p',markerfacecolor='white',markeredgecolor='royalblue', markeredgewidth=2, markersize=15)
#ax2.plot(x, y4,'-',color='darkgreen',linewidth=4, label='SMART (8)',marker=u'v',markerfacecolor='white',markeredgecolor='darkgreen', markeredgewidth=2, markersize=15)
#ax2.plot(x, y5,'-',color='olive',linewidth=4, label='SMART (15)',marker=u'^',markerfacecolor='white',markeredgecolor='olive', markeredgewidth=2, markersize=15)

ax2.plot(x, y6,'-',color='tab:red',linewidth=4, label='TNT: Minimum',marker=u'o',markerfacecolor='white',markeredgecolor='tab:red', markeredgewidth=2, markersize=15)
ax2.plot(x, y7,'-',color='tab:blue',linewidth=4, label='TNT: Typical',marker=u's',markerfacecolor='white',markeredgecolor='tab:blue', markeredgewidth=2, markersize=15)
ax2.plot(x, y8,'-',color='tab:green',linewidth=4, label='TNT: Maximum',marker=u'p',markerfacecolor='white',markeredgecolor='tab:green', markeredgewidth=2, markersize=15)
#ax2.plot(x, y9,'-',color='darkorange',linewidth=4, label='TNT:N (8)',marker=u'v',markerfacecolor='white',markeredgecolor='darkorange', markeredgewidth=2, markersize=15)
#ax2.plot(x, y10,'-',color='magenta',linewidth=4, label='TNT:v (15)',marker=u'^',markerfacecolor='white',markeredgecolor='magenta', markeredgewidth=2, markersize=15)

#ax2.plot(x, y11,'-',color='gold',linewidth=4, label='ONLY-WIRE (2)')
ax2.plot(x, y12,'-',color='gold',linewidth=4, label='IDEAL 1-cyc')

ax2.yaxis.set_major_locator(ticker.MultipleLocator(4))
ax2.yaxis.grid(True)

h,l = ax2.get_legend_handles_labels()

ax2.legend(h, l,loc='upper left', ncol=1)

vals = ax2.get_yticks()
#ax2.set_xticklabels(['{:3.0f}'.format(x) for x in vals])
#ax2.set_yticklabels(['{:3.0f}'.format(x) for x in vals])
plt.xlim(0, 0.25)
plt.ylim(0.1, 40)
#plt.yticks(np.arange(min(x), max(x)+1, 1.0))
#ax2.set_xticks([1, 4, 16, 64, 256])
#ax2.set(xlabel="Number of uniquely configured LUTs",ylabel="Percentage Increase in Speedup (rel. 1 LUT)")
ax2.set_xlabel("Injection Rate (flits/node/cycle)",fontsize=48)
ax2.set_ylabel("Average flit latency (cycles)",fontsize=48)
#########################

plt.show()

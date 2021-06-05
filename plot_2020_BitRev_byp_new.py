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
y0 = np.array([12.878790, 12.928035, 13.041121, 13.139899, 13.342688, 13.622865, 14.084587, 15.148697, 28.309818, 177.981809, 325.614822, 492.186096, 733.809873, 964.104614, 1141.212793, 1288.717642, 1439.379346, 1569.855481, 1689.779259, 1804.820432, 1926.905333, 2026.117033, 2096.192917, 2193.118389, 2269.016137])
#s
#y1=np.array([15.841985,15.925818,16.203575,16.261470,16.414911,16.519860,16.696600,16.971992,17.194129,17.515001,17.863588,18.521922,19.579682,23.716667,114.401260,303.273427,475.982530,671.896371,816.461257,1006.481345,1158.508684,1299.377256,1434.924839,1593.027771,1736.775331])
#y2=np.array([8.752877,8.873096,9.080524,9.202275,9.357376,9.492218,9.678108,9.894073,10.116519,10.379988,10.629412,10.998586,11.413593,12.045236,12.969750,15.585625,47.921177,219.487903,399.625183,573.624309,713.731005,861.584739,1015.271608,1155.351814,1307.480652])
#y3=np.array([5.246197,5.399103,5.616084,5.774054,5.958247,6.164364,6.389695,6.626899,6.903403,7.214344,7.511635,7.911074,8.349227,8.965828,9.800313,11.442370,22.021091,154.527040,319.364270,508.023240,660.956264,793.551966,964.592470,1080.141761,1244.314051])
#y4=np.array([3.536407,3.743194,3.983580,4.200913,4.479322,4.736035,5.086452,5.427490,5.783416,6.231383,6.675092,7.161476,7.744273,8.537415,9.535777,11.673363,29.380938,188.207640,334.644517,527.566642,686.416151,828.991033,970.555356,1136.934148,1296.693703])
#y5=np.array([3.193223,3.418270,3.689828,3.933919,4.240337,4.538822,4.914905,5.292504,5.683973,6.162574,6.623518,7.148901,7.757402,8.576372,9.663299,11.639939,34.330371,190.557146,340.556823,556.041505,682.808358,844.228688,992.130093,1125.984756,1284.217693])

#m
y6=np.array([6.348473, 7.316228, 8.318771, 9.317436, 10.513903, 11.712454, 13.380615, 19.028543, 182.458048, 485.592967, 873.782731, 1117.381025, 1315.114039, 1476.660164, 1598.095636, 1722.765703, 1878.766602, 2000.174685, 2111.513097, 2227.781519, 2311.796898, 2394.653811, 2476.569146, 2551.648696, 2655.755443])
y7=np.array([5.122934, 5.717891, 6.338922, 7.005757, 7.799245, 8.696551, 9.909137, 12.772761, 97.759962, 385.667634, 841.083377, 1083.169514, 1274.803263, 1443.609667, 1584.844674, 1695.777938, 1830.835747, 1966.124219, 2079.115880, 2181.461630, 2291.775715, 2376.478031, 2443.699545, 2527.306399, 2631.642326])
y8=np.array([3.366326, 3.773742, 4.230769, 4.761546, 5.422636, 6.223614, 7.391059, 9.538574, 66.883019, 372.112862, 838.037298, 1083.489514, 1275.654114, 1435.377728, 1567.639045, 1688.018179, 1817.811202, 1947.002824, 2078.673142, 2187.339352, 2281.612971, 2357.906205, 2443.347519, 2515.896283, 2613.708392])
#y9=np.array([3.432545,3.644715,3.903281,4.128557,4.410901,4.690064,5.053193,5.412761,5.770937,6.251254,6.675499,7.219559,7.812012,8.594203,9.695536,11.796995,33.985263,176.112580,349.579538,541.253947,692.518799,828.130612,989.986754,1128.713404,1288.924860])
#y10=np.array([3.193223,3.418270,3.689828,3.933919,4.240337,4.538822,4.914905,5.292504,5.683973,6.162574,6.623518,7.148901,7.757402,8.576372,9.663299,11.639939,34.330371,190.557146,340.556823,556.041505,682.808358,844.228688,992.130093,1125.984756,1284.217693])


#ideal1
#y11 = np.array([5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,1000])
#y12 = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1000])

ax2.plot(x, y0,'-',color='black',linewidth=4, label='BASE 1-c rtr',marker=u'x',markerfacecolor='white',markeredgecolor='black', markeredgewidth=2, markersize=15)

#ax2.plot(x, y1,'-',color='darkblue',linewidth=4, label='SMART (1)',marker=u'o',markerfacecolor='white',markeredgecolor='darkblue', markeredgewidth=2, markersize=15)
#ax2.plot(x, y2,'-',color='blue',linewidth=4, label='SMART (2)',marker=u's',markerfacecolor='white',markeredgecolor='blue', markeredgewidth=2, markersize=15)
#ax2.plot(x, y3,'-',color='royalblue',linewidth=4, label='SMART (4)',marker=u'p',markerfacecolor='white',markeredgecolor='royalblue', markeredgewidth=2, markersize=15)
#ax2.plot(x, y4,'-',color='darkgreen',linewidth=4, label='SMART (8)',marker=u'v',markerfacecolor='white',markeredgecolor='darkgreen', markeredgewidth=2, markersize=15)
#ax2.plot(x, y5,'-',color='olive',linewidth=4, label='SMART (15)',marker=u'^',markerfacecolor='white',markeredgecolor='olive', markeredgewidth=2, markersize=15)

ax2.plot(x, y6,'-',color='darkred',linewidth=4, label='TNT: Minium',marker=u'o',markerfacecolor='white',markeredgecolor='darkred', markeredgewidth=2, markersize=15)
ax2.plot(x, y7,'-',color='red',linewidth=4, label='TNT: Typical',marker=u's',markerfacecolor='white',markeredgecolor='red', markeredgewidth=2, markersize=15)
ax2.plot(x, y8,'-',color='saddlebrown',linewidth=4, label='TNT: Maximum',marker=u'p',markerfacecolor='white',markeredgecolor='saddlebrown', markeredgewidth=2, markersize=15)
#ax2.plot(x, y9,'-',color='darkorange',linewidth=4, label='TNT:N (8)',marker=u'v',markerfacecolor='white',markeredgecolor='darkorange', markeredgewidth=2, markersize=15)
#ax2.plot(x, y10,'-',color='magenta',linewidth=4, label='TNT:v (15)',marker=u'^',markerfacecolor='white',markeredgecolor='magenta', markeredgewidth=2, markersize=15)

#ax2.plot(x, y11,'-',color='gold',linewidth=4, label='ONLY-WIRE (2)')
#ax2.plot(x, y12,'-',color='magenta',linewidth=4, label='ONLY-WIRE (8)')

ax2.yaxis.set_major_locator(ticker.MultipleLocator(4))
ax2.yaxis.grid(True)

h,l = ax2.get_legend_handles_labels()

ax2.legend(h, l,loc='upper right', ncol=1)

vals = ax2.get_yticks()
#ax2.set_xticklabels(['{:3.0f}'.format(x) for x in vals])
#ax2.set_yticklabels(['{:3.0f}'.format(x) for x in vals])
plt.xlim(0, 0.5)
plt.ylim(0.1, 32)
#plt.yticks(np.arange(min(x), max(x)+1, 1.0))
#ax2.set_xticks([1, 4, 16, 64, 256])
#ax2.set(xlabel="Number of uniquely configured LUTs",ylabel="Percentage Increase in Speedup (rel. 1 LUT)")
ax2.set_xlabel("Injection Rate (flits/node/cycle)",fontsize=48)
ax2.set_ylabel("Average flit latency (cycles)",fontsize=48)
#########################

plt.show()

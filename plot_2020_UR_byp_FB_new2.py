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



x = np.array([0.02,0.04,0.06,0.08,0.10,0.12,0.14,0.16,0.18,0.20,0.22,0.24,0.26,0.28,0.30,0.32,0.34,0.36,0.38,0.40,0.42,0.44,0.46,0.48,0.50,0.52,0.54,0.56,0.58,0.60,0.62,0.64,0.66,0.68,0.70,0.72,0.74,0.76,0.78,0.80,0.82,0.84,0.86,0.88,0.90,0.92,0.94,0.96,0.98,1])

#base
y0=np.array([5.174324+0.5, 5.322710+0.5, 5.504784+0.5, 5.659676+0.5, 5.861955+0.5, 6.017567+0.5, 6.227467+0.5, 6.434660+0.5, 6.632714+0.5, 6.865850+0.5, 7.092457+0.5, 7.365605+0.5, 7.640135+0.5, 7.987339+0.5, 8.341059+0.5, 8.780287+0.5, 9.241147+0.5, 9.855531+0.5, 10.687197+0.5, 11.814650+0.5, 14.055006+0.5, 35.197231+0.5, 149.319282, 290.865626, 443.845254, 577.299938, 707.546060, 831.724046, 966.268994, 1087.514361, 1207.870282, 1327.250907, 1426.013984, 1525.518506, 1635.346665, 1709.515061, 1791.862454, 1892.305448, 1971.494500, 2038.653175, 2102.908258, 2183.309084, 2252.136172, 2318.586470, 2377.988615, 2417.484317, 2496.779048, 2543.061842, 2563.600950, 2613.420263])
#s
#y1=np.array([15.841985,15.925818,16.203575,16.261470,16.414911,16.519860,16.696600,16.971992,17.194129,17.515001,17.863588,18.521922,19.579682,23.716667,114.401260,303.273427,475.982530,671.896371,816.461257,1006.481345,1158.508684,1299.377256,1434.924839,1593.027771,1736.775331])
#y2=np.array([8.752877,8.873096,9.080524,9.202275,9.357376,9.492218,9.678108,9.894073,10.116519,10.379988,10.629412,10.998586,11.413593,12.045236,12.969750,15.585625,47.921177,219.487903,399.625183,573.624309,713.731005,861.584739,1015.271608,1155.351814,1307.480652])
#y3=np.array([5.246197,5.399103,5.616084,5.774054,5.958247,6.164364,6.389695,6.626899,6.903403,7.214344,7.511635,7.911074,8.349227,8.965828,9.800313,11.442370,22.021091,154.527040,319.364270,508.023240,660.956264,793.551966,964.592470,1080.141761,1244.314051])
#y4=np.array([3.536407,3.743194,3.983580,4.200913,4.479322,4.736035,5.086452,5.427490,5.783416,6.231383,6.675092,7.161476,7.744273,8.537415,9.535777,11.673363,29.380938,188.207640,334.644517,527.566642,686.416151,828.991033,970.555356,1136.934148,1296.693703])
#y5=np.array([3.193223,3.418270,3.689828,3.933919,4.240337,4.538822,4.914905,5.292504,5.683973,6.162574,6.623518,7.148901,7.757402,8.576372,9.663299,11.639939,34.330371,190.557146,340.556823,556.041505,682.808358,844.228688,992.130093,1125.984756,1284.217693])

#m
y6=np.array([5.514660+0.5, 5.514892+0.5, 5.537226+0.5, 5.539689+0.5, 5.555399+0.5, 5.558580+0.5, 5.577862+0.5, 5.597536+0.5, 5.608651+0.5, 5.623674+0.5, 5.643189+0.5, 5.658344+0.5, 5.672485+0.5, 5.693509+0.5, 5.720692+0.5, 5.740067+0.5, 5.757777+0.5, 5.783580+0.5, 5.806060+0.5, 5.839882+0.5, 5.865824+0.5, 5.898466+0.5, 5.935394+0.5, 5.975341+0.5, 6.013076+0.5, 6.056020+0.5, 6.098760+0.5, 6.158985+0.5, 6.218019+0.5, 6.287421+0.5, 6.359066+0.5, 6.443846+0.5, 6.541571+0.5, 6.649012+0.5, 6.783904+0.5, 6.944637+0.5, 7.100404+0.5, 7.306154+0.5, 7.599367+0.5, 7.938707+0.5, 8.372328+0.5, 9.053888+0.5, 9.909459+0.5, 11.478472+0.5, 17.305328+0.5, 36.874123, 80.135993, 152.441598, 245.283145, 352.361026])
y7=np.array([8.041977+0.5, 8.079236+0.5, 8.136746+0.5, 8.184198+0.5, 8.247779+0.5, 8.309949+0.5, 8.392041+0.5, 8.495059+0.5, 8.598533+0.5, 8.733122+0.5, 8.885154+0.5, 9.084189+0.5, 9.290517+0.5, 9.566849+0.5, 9.927007+0.5, 10.355689+0.5, 10.932135+0.5, 11.668503+0.5, 12.901850+0.5, 14.502142+0.5, 17.721325+0.5, 27.396404+0.5, 63.068574, 216.828448, 396.943625, 582.437650, 744.979520, 900.356902, 1037.720043, 1163.508718, 1297.449060, 1405.931684, 1520.903274, 1624.428887, 1718.667286, 1812.029880, 1901.013125, 1976.388040, 2058.177029, 2129.815714, 2192.535910, 2256.171056, 2319.991941, 2376.658229, 2434.549974, 2491.720646, 2543.171572, 2593.233789, 2646.818064, 2698.766449])
y8=np.array([20.712167+0.5, 21.135637+0.5, 22.279626+0.5, 25.062459+0.5, 31.650628+0.5, 68.284270+0.5, 575.358079, 1102.490769, 1545.455094, 1895.468827, 2173.615333, 2424.860664, 2614.980505, 2783.532599, 2921.158870, 3060.301711, 3165.749347, 3269.505090, 3358.283528, 3432.819995, 3502.027228, 3578.294369, 3643.351916, 3702.525394, 3756.703397, 3806.877662, 3854.304876, 3895.062206, 3930.590698, 3959.142713, 3998.444787, 4035.857676, 4068.572656, 4084.657023, 4113.418945, 4140.525315, 4162.537569, 4166.830114, 4202.609129, 4217.851710, 4245.612472, 4250.972127, 4265.684427, 4286.870569, 4293.787235, 4319.845042, 4331.817862, 4344.503081, 4357.727105, 4378.776034])
#y9=np.array([3.432545,3.644715,3.903281,4.128557,4.410901,4.690064,5.053193,5.412761,5.770937,6.251254,6.675499,7.219559,7.812012,8.594203,9.695536,11.796995,33.985263,176.112580,349.579538,541.253947,692.518799,828.130612,989.986754,1128.713404,1288.924860])
#y10=np.array([3.193223,3.418270,3.689828,3.933919,4.240337,4.538822,4.914905,5.292504,5.683973,6.162574,6.623518,7.148901,7.757402,8.576372,9.663299,11.639939,34.330371,190.557146,340.556823,556.041505,682.808358,844.228688,992.130093,1125.984756,1284.217693])


#ideal1
#y11 = np.array([5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,5.33/2,1000])
#y12 = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1000])

ax2.plot(x, y0,'-',color='tab:red',linewidth=4, label='TNT',marker=u'x',markerfacecolor='white',markeredgecolor='tab:red', markeredgewidth=2, markersize=15)

#ax2.plot(x, y1,'-',color='darkblue',linewidth=4, label='SMART (1)',marker=u'o',markerfacecolor='white',markeredgecolor='darkblue', markeredgewidth=2, markersize=15)
#ax2.plot(x, y2,'-',color='blue',linewidth=4, label='SMART (2)',marker=u's',markerfacecolor='white',markeredgecolor='blue', markeredgewidth=2, markersize=15)
#ax2.plot(x, y3,'-',color='royalblue',linewidth=4, label='SMART (4)',marker=u'p',markerfacecolor='white',markeredgecolor='royalblue', markeredgewidth=2, markersize=15)
#ax2.plot(x, y4,'-',color='darkgreen',linewidth=4, label='SMART (8)',marker=u'v',markerfacecolor='white',markeredgecolor='darkgreen', markeredgewidth=2, markersize=15)
#ax2.plot(x, y5,'-',color='olive',linewidth=4, label='SMART (15)',marker=u'^',markerfacecolor='white',markeredgecolor='olive', markeredgewidth=2, markersize=15)

ax2.plot(x, y6,'-',color='tab:blue',linewidth=4, label='FB (BB=7x)',marker=u'o',markerfacecolor='white',markeredgecolor='tab:blue', markeredgewidth=2, markersize=15)
ax2.plot(x, y7,'-',color='tab:orange',linewidth=4, label='FB (BB=3.5x)',marker=u's',markerfacecolor='white',markeredgecolor='tab:orange', markeredgewidth=2, markersize=15)
ax2.plot(x, y8,'-',color='tab:green',linewidth=4, label='FB (BB=1x)',marker=u'p',markerfacecolor='white',markeredgecolor='tab:green', markeredgewidth=2, markersize=15)
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
plt.xlim(0, 1)
plt.ylim(0.1, 32)
#plt.yticks(np.arange(min(x), max(x)+1, 1.0))
#ax2.set_xticks([1, 4, 16, 64, 256])
#ax2.set(xlabel="Number of uniquely configured LUTs",ylabel="Percentage Increase in Speedup (rel. 1 LUT)")
ax2.set_xlabel("Injection Rate (flits/node/cycle)",fontsize=48)
ax2.set_ylabel("Average flit latency",fontsize=48)
#########################

plt.show()
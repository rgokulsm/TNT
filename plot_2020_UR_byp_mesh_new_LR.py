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



x = np.array([200*0.02,200*0.04,200*0.06,200*0.08,200*0.10,200*0.12,200*0.14,200*0.16,200*0.18,200*0.20,200*0.22,200*0.24,200*0.26,200*0.28,200*0.30,200*0.32,200*0.34,200*0.36,200*0.38,200*0.40,200*0.42,200*0.44,200*0.46,200*0.48,200*0.50])

#s
hpc=1
y1=np.array([1*(5.234774*hpc-5)/5,1*(5.221050*hpc-5)/5,1*(5.273643*hpc-5)/5,1*(5.250854*hpc-5)/5,1*(5.255628*hpc-5)/5,1*(5.241831*hpc-5)/5,1*(5.239943*hpc-5)/5,1*(5.259477*hpc-5)/5,1*(5.253064*hpc-5)/5,1*(5.251858*hpc-5)/5,1*(5.238226*hpc-5)/5,1*(5.244220*hpc-5)/5,1*(5.244951*hpc-5)/5,1*(5.252441*hpc-5)/5,1*(5.248747*hpc-5)/5,1*(5.241988*hpc-5)/5,1*(5.220726*hpc-5)/5,1*(5.210255*hpc-5)/5,1*(5.206404*hpc-5)/5,1*(5.185809*hpc-5)/5,1*(5.183182*hpc-5)/5,1*(5.178969*hpc-5)/5,1*(5.183977*hpc-5)/5,1*(5.181767*hpc-5)/5,1*(5.172504*hpc-5)/5])
hpc=2
y2=np.array([1*(2.886726*hpc-5)/5,1*(2.903632*hpc-5)/5,1*(2.954575*hpc-5)/5,1*(2.972664*hpc-5)/5,1*(3.003238*hpc-5)/5,1*(3.025678*hpc-5)/5,1*(3.059571*hpc-5)/5,1*(3.105731*hpc-5)/5,1*(3.143902*hpc-5)/5,1*(3.193653*hpc-5)/5,1*(3.234598*hpc-5)/5,1*(3.294265*hpc-5)/5,1*(3.358184*hpc-5)/5,1*(3.444215*hpc-5)/5,1*(3.536577*hpc-5)/5,1*(3.674235*hpc-5)/5,1*(3.839019*hpc-5)/5,1*(3.940711*hpc-5)/5,1*(3.968851*hpc-5)/5,1*(3.966179*hpc-5)/5,1*(3.962869*hpc-5)/5,1*(3.963621*hpc-5)/5,1*(3.966382*hpc-5)/5,1*(3.956433*hpc-5)/5,1*(3.939698*hpc-5)/5])
hpc=4
y3=np.array([1*(1.719284*hpc-5)/5,1*(1.752134*hpc-5)/5,1*(1.810297*hpc-5)/5,1*(1.844103*hpc-5)/5,1*(1.887954*hpc-5)/5,1*(1.933657*hpc-5)/5,1*(1.985175*hpc-5)/5,1*(2.041893*hpc-5)/5,1*(2.100690*hpc-5)/5,1*(2.168473*hpc-5)/5,1*(2.232572*hpc-5)/5,1*(2.319344*hpc-5)/5,1*(2.407721*hpc-5)/5,1*(2.526026*hpc-5)/5,1*(2.661721*hpc-5)/5,1*(2.846745*hpc-5)/5,1*(3.121798*hpc-5)/5,1*(3.357267*hpc-5)/5,1*(3.443272*hpc-5)/5,1*(3.463027*hpc-5)/5,1*(3.459801*hpc-5)/5,1*(3.460119*hpc-5)/5,1*(3.459876*hpc-5)/5,1*(3.468256*hpc-5)/5,1*(3.435083*hpc-5)/5])
hpc=8
y4=np.array([1*(1.150276*hpc-5)/5,1*(1.200197*hpc-5)/5,1*(1.265645*hpc-5)/5,1*(1.316871*hpc-5)/5,1*(1.386557*hpc-5)/5,1*(1.447664*hpc-5)/5,1*(1.532649*hpc-5)/5,1*(1.617798*hpc-5)/5,1*(1.699871*hpc-5)/5,1*(1.807795*hpc-5)/5,1*(1.911741*hpc-5)/5,1*(2.023597*hpc-5)/5,1*(2.156005*hpc-5)/5,1*(2.324711*hpc-5)/5,1*(2.514004*hpc-5)/5,1*(2.774094*hpc-5)/5,1*(3.148459*hpc-5)/5,1*(3.403023*hpc-5)/5,1*(3.481899*hpc-5)/5,1*(3.503942*hpc-5)/5,1*(3.502346*hpc-5)/5,1*(3.516065*hpc-5)/5,1*(3.508310*hpc-5)/5,1*(3.498726*hpc-5)/5,1*(3.490332*hpc-5)/5])
y5=np.array([])



#m
y6=np.array([1*(2.467408*5-5)/5,1*(2.514521*5-5)/5,1*(2.592897*5-5)/5,1*(2.641489*5-5)/5,1*(2.699942*5-5)/5,1*(2.748781*5-5)/5,1*(2.811942*5-5)/5,1*(2.885112*5-5)/5,1*(2.947582*5-5)/5,1*(3.024528*5-5)/5,1*(3.099970*5-5)/5,1*(3.192228*5-5)/5,1*(3.290197*5-5)/5,1*(3.421644*5-5)/5,1*(3.576328*5-5)/5,1*(3.827915*5-5)/5,1*(3.992899*5-5)/5,1*(4.071537*5-5)/5,1*(4.083070*5-5)/5,1*(4.069850*5-5)/5,1*(4.072248*5-5)/5,1*(4.075947*5-5)/5,1*(4.074044*5-5)/5,1*(4.073183*5-5)/5,1*(4.045809*5-5)/5])
y7=np.array([1*(1.842856*5-5)/5,1*(1.888648*5-5)/5,1*(1.964359*5-5)/5,1*(2.009723*5-5)/5,1*(2.069270*5-5)/5,1*(2.122284*5-5)/5,1*(2.192460*5-5)/5,1*(2.262997*5-5)/5,1*(2.328768*5-5)/5,1*(2.410274*5-5)/5,1*(2.490813*5-5)/5,1*(2.586328*5-5)/5,1*(2.689059*5-5)/5,1*(2.823969*5-5)/5,1*(2.980842*5-5)/5,1*(3.205009*5-5)/5,1*(3.524026*5-5)/5,1*(3.677835*5-5)/5,1*(3.721681*5-5)/5,1*(3.722686*5-5)/5,1*(3.725460*5-5)/5,1*(3.723105*5-5)/5,1*(3.731309*5-5)/5,1*(3.726567*5-5)/5,1*(3.704626*5-5)/5])
y8=np.array([1*(1.382536*5-5)/5,1*(1.434434*5-5)/5,1*(1.500000*5-5)/5,1*(1.546616*5-5)/5,1*(1.612422*5-5)/5,1*(1.668587*5-5)/5,1*(1.744607*5-5)/5,1*(1.819108*5-5)/5,1*(1.893916*5-5)/5,1*(1.985926*5-5)/5,1*(2.075421*5-5)/5,1*(2.179314*5-5)/5,1*(2.302023*5-5)/5,1*(2.455750*5-5)/5,1*(2.632692*5-5)/5,1*(2.878770*5-5)/5,1*(3.224126*5-5)/5,1*(3.462579*5-5)/5,1*(3.532756*5-5)/5,1*(3.542894*5-5)/5,1*(3.552412*5-5)/5,1*(3.546550*5-5)/5,1*(3.557066*5-5)/5,1*(3.554854*5-5)/5,1*(3.542286*5-5)/5])
y9=np.array([1*(1.078487*8-5)/5,1*(1.134073*8-5)/5,1*(1.205531*8-5)/5,1*(1.260582*8-5)/5,1*(1.335272*8-5)/5,1*(1.403675*8-5)/5,1*(1.494787*8-5)/5,1*(1.585712*8-5)/5,1*(1.672002*8-5)/5,1*(1.791391*8-5)/5,1*(1.894490*8-5)/5,1*(2.022874*8-5)/5,1*(2.158068*8-5)/5,1*(2.330102*8-5)/5,1*(2.533904*8-5)/5,1*(2.793009*8-5)/5,1*(3.167733*8-5)/5,1*(3.414570*8-5)/5,1*(3.507297*8-5)/5,1*(3.509624*8-5)/5,1*(3.515555*8-5)/5,1*(3.520180*8-5)/5,1*(3.524127*8-5)/5,1*(3.521946*8-5)/5,1*(3.499748*8-5)/5])
y10=np.array([])



#ax2.plot(x, y0,'-',color='black',linewidth=4, label='BASE 1-c rtr',marker=u'x',markerfacecolor='white',markeredgecolor='black', markeredgewidth=2, markersize=15)

#ax2.plot(x, y1,'-',color='darkblue',linewidth=4, label='SMART (1)',marker=u'o',markerfacecolor='white',markeredgecolor='darkblue', markeredgewidth=2, markersize=15)
#ax2.plot(x, y2,'-',color='blue',linewidth=4, label='SMART (2)',marker=u's',markerfacecolor='white',markeredgecolor='blue', markeredgewidth=2, markersize=15)
#ax2.plot(x, y3,'-',color='royalblue',linewidth=4, label='SMART (4)',marker=u'p',markerfacecolor='white',markeredgecolor='royalblue', markeredgewidth=2, markersize=15)
#ax2.plot(x, y4,'-',color='darkgreen',linewidth=4, label='SMART (8)',marker=u'v',markerfacecolor='white',markeredgecolor='darkgreen', markeredgewidth=2, markersize=15)
#ax2.plot(x, y5,'-',color='olive',linewidth=4, label='SMART (15)',marker=u'^',markerfacecolor='white',markeredgecolor='olive', markeredgewidth=2, markersize=15)

ax2.plot(x, y6,'-',color='tab:red',linewidth=4, label='$\eta_{chip} = 1$',marker=u'o',markerfacecolor='white',markeredgecolor='tab:red', markeredgewidth=2, markersize=15)
ax2.plot(x, y7,'-',color='tab:blue',linewidth=4, label='$\eta_{chip} = 0.5$',marker=u's',markerfacecolor='white',markeredgecolor='tab:blue', markeredgewidth=2, markersize=15)
ax2.plot(x, y8,'-',color='tab:green',linewidth=4, label='$\eta_{chip} = 0.25$',marker=u'p',markerfacecolor='white',markeredgecolor='tab:green', markeredgewidth=2, markersize=15)
ax2.plot(x, y9,'-',color='tab:orange',linewidth=4, label='$\eta_{chip} = 0.125$',marker=u'v',markerfacecolor='white',markeredgecolor='tab:orange', markeredgewidth=2, markersize=15)
#ax2.plot(x, y10,'-',color='magenta',linewidth=4, label='TNT:v (15)',marker=u'^',markerfacecolor='white',markeredgecolor='magenta', markeredgewidth=2, markersize=15)

#ax2.plot(x, y11,'-',color='gold',linewidth=4, label='IDEAL 1-c ntwk')

#ax2.yaxis.set_major_locator(ticker.MultipleLocator(4))
ax2.yaxis.grid(True)

h,l = ax2.get_legend_handles_labels()

ax2.legend(h, l,loc='upper left', ncol=1)

vals = ax2.get_yticks()
plt.yticks([1, 2, 3, 4], ['1x', '2x', '3x', '4x'])
#ax2.set_xticklabels(['{:3.0f}'.format(x) for x in vals])
#ax2.set_yticklabels(['{:3.0f}'.format(x) for x in vals])
plt.xlim(0, 200*0.5)
#plt.ylim(0, 20)
#plt.yticks(np.arange(min(x), max(x)+1, 1.0))
#ax2.set_xticks([1, 4, 16, 64, 256])
#ax2.set(xlabel="Number of uniquely configured LUTs",ylabel="Percentage Increase in Speedup (rel. 1 LUT)")
ax2.set_xlabel("Injection Rate (% of Capacity)",fontsize=48)
ax2.set_ylabel("Reduction in LR (vs pt-pt)",fontsize=48)
#########################

plt.show()
                                     




import pandas as pd
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, read_csv
import matplotlib.ticker as ticker


plt.rcParams.update({'font.size': 28})

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



x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

y1 = np.array([4.04E+01,3.98E+01,3.96E+01,3.96E+01,3.97E+01,3.98E+01,4.02E+01,4.04E+01,4.07E+01,4.15E+01,4.17E+01,4.26E+01,4.27E+01,4.33E+01,4.53E+01,4.60E+01,4.67E+01,4.73E+01,4.88E+01,5.01E+01])
y2 = np.array([4.01E+01,4.04E+01,4.23E+01,4.60E+01,5.01E+01,5.89E+01])
y3 = np.array([4.07E+01,4.83E+01])
y4 = np.array([4.49E+01])

y5 = np.array([3.24E+01,3.21E+01,3.20E+01,3.21E+01,3.21E+01,3.22E+01,3.25E+01,3.27E+01,3.26E+01,3.33E+01,3.31E+01,3.36E+01,3.41E+01,3.40E+01,3.51E+01,3.55E+01,3.59E+01,3.62E+01,3.70E+01,3.72E+01])
y6 = np.array([3.22E+01,3.27E+01,3.34E+01,3.55E+01,3.77E+01,4.17E+01])
y7 = np.array([3.30E+01,3.68E+01])
y8 = np.array([3.49E+01])

y9 = np.array([2.36E+01,2.34E+01,2.34E+01,2.34E+01,2.35E+01,2.35E+01,2.36E+01,2.37E+01,2.38E+01,2.39E+01,2.39E+01,2.41E+01,2.43E+01,2.45E+01,2.48E+01,2.49E+01,2.51E+01,2.52E+01,2.54E+01,2.57E+01])
y10 = np.array([2.36E+01,2.37E+01,2.40E+01,2.49E+01,2.59E+01,2.73E+01])
y11 = np.array([2.39E+01,2.55E+01])
y12 = np.array([2.47E+01])

ax2.plot(x, y1,'-',color='red',linewidth=8, label='45nm / 1GHz',marker=u'o',markerfacecolor='white',markeredgecolor='red', markeredgewidth=4, markersize=20)
ax2.plot(x[0:6], y2,'-',color='red',linewidth=8, label='45nm / 2GHz',marker=u's',markerfacecolor='white',markeredgecolor='red', markeredgewidth=4, markersize=20)
ax2.plot(x[0:2], y3,'-',color='red',linewidth=8, label='45nm / 3GHz',marker=u'd',markerfacecolor='white',markeredgecolor='red', markeredgewidth=4, markersize=20)
#ax2.plot(x[0:1], y4,'-',color='red',linewidth=8, label='45nm / 4GHz',marker=u'x',markerfacecolor='white',markeredgecolor='red', markeredgewidth=4, markersize=20)

ax2.plot(x, y5,'-',color='blue',linewidth=8, label='32nm / 1GHz',marker=u'o',markerfacecolor='white',markeredgecolor='blue', markeredgewidth=4, markersize=20)
ax2.plot(x[0:6], y6,'-',color='blue',linewidth=8, label='32nm / 2GHz',marker=u's',markerfacecolor='white',markeredgecolor='blue', markeredgewidth=4, markersize=20)
ax2.plot(x[0:2], y7,'-',color='blue',linewidth=8, label='32nm / 3GHz',marker=u'd',markerfacecolor='white',markeredgecolor='blue', markeredgewidth=4, markersize=20)
#ax2.plot(x[0:1], y8,'-',color='blue',linewidth=8, label='32nm / 4GHz',marker=u'x',markerfacecolor='white',markeredgecolor='blue', markeredgewidth=4, markersize=20)

ax2.plot(x, y9,'-',color='green',linewidth=8, label='22nm / 1GHz',marker=u'o',markerfacecolor='white',markeredgecolor='green', markeredgewidth=4, markersize=20)
ax2.plot(x[0:6], y10,'-',color='green',linewidth=8, label='22nm / 2GHz',marker=u's',markerfacecolor='white',markeredgecolor='green', markeredgewidth=4, markersize=20)
ax2.plot(x[0:2], y11,'-',color='green',linewidth=8, label='22nm / 3GHz',marker=u'd',markerfacecolor='white',markeredgecolor='green', markeredgewidth=4, markersize=20)
#ax2.plot(x[0:1], y12,'-',color='green',linewidth=8, label='22nm / 4GHz',marker=u'x',markerfacecolor='white',markeredgecolor='green', markeredgewidth=4, markersize=20)

ax2.yaxis.set_major_locator(ticker.MultipleLocator(3))
#ax2.yaxis.set_minor_locator(ticker.MultipleLocator(2))
ax2.yaxis.grid(True)
ax2.xaxis.grid(True)
ax2.xaxis.set_major_locator(ticker.MultipleLocator(1))
#ax2.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))

h,l = ax2.get_legend_handles_labels()

ax2.legend(h, l,loc='upper right', ncol=3)

vals = ax2.get_yticks()
#ax2.set_xticklabels(['{:3.0f}'.format(x) for x in vals])
#ax2.set_yticklabels(['{:3.0f}'.format(x) for x in vals])
plt.xlim(0, 20.5)
plt.ylim(20, 60)
#plt.yticks(np.arange(min(x), max(x)+1, 1.0))
#ax2.set_xticks([1, 4, 16, 64, 256])
#ax2.set(xlabel="Number of uniquely configured LUTs",ylabel="Percentage Increase in Speedup (rel. 1 LUT)")
ax2.set_xlabel("Length (mm)",fontsize=32)
ax2.set_ylabel("Energy (fJ/bit/mm)",fontsize=32)
#########################

plt.show()

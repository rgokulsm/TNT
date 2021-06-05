import pandas as pd
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 28})
#fig_size = plt.rcParams["figure.figsize"]
#print "Current size:", fig_size
#fig_size[0] = 12
#plt.rcParams["figure.figsize"] = fig_size
#print "Current size:", fig_size
hatches=['O', '//', None, '\\\\', '.', 'x', None,'////']
colors = ['0.95','0.75','0.55','0.35','0.15']
colors2 = [(1,0,0),(0.7,0,0),(0.4,0,0),(0.1,0,0)]
colors = ['silver' ,'silver','silver','silver','silver']
colors2 = ['tomato','tomato','tomato','tomato','tomato']
def plot_clustered_stacked(dfall, labels=None, title=" " ,  H="/", **kwargs):
    """Given a list of dataframes, with identical columns and index, create a clustered stacked bar plot. 
labels is a list of the names of the dataframe, used for the legend
title is a string for the title of the plot
H is the hatch used for identification of the different dataframe"""

    n_df = len(dfall)
    n_col = len(dfall[0].columns)
    n_ind = len(dfall[0].index)
    axe = plt.subplot(111)

    for df in dfall : # for each data frame
        axe = df.plot(kind="bar",
                      linewidth=0,
                      stacked=True,
                      ax=axe,
                      legend=False,
                      grid=False,
                      **kwargs)  # make bar plots

    h,l = axe.get_legend_handles_labels() # get the handles we want to modify
    for i in range(0, n_df * n_col, 1): # len(h) = n_col * n_df
        for j, pa in enumerate(h[i:i+n_col]):
            for rect in pa.patches: # for each index
                #rect.set_x(rect.get_x() + 1 / float(n_df + 1) * n_col / float(n_col))
                #rect.set_hatch(H * int(i / n_col)) #edited part     
                rect.set_hatch(hatches[i])
                if(i <= 4): rect.set_color(colors[i])
                if(i>4): rect.set_color(colors2[i-5])
                rect.set_linewidth(2)
                rect.set_edgecolor('black')
                rect.set_width(1 / float(n_df + 1))

    axe.set_xticks((np.arange(0, 2 * n_ind, 2) + 0 / float(n_df + 1)) / 2.)
    axe.set_xticklabels(df.index, rotation = 0)
    #axe.set_yticks(np.arange(0,50,10))
    #axe.set_title(title)
    #axe.set(xlabel="Baseline vs. SMART (HPC) vs. TNT (HPC)",ylabel="Access Energy (fJ/bit/mm)")
    axe.set(ylabel="Access Energy (fJ/bit/mm)")


    # Add invisible data to add another legend
    n=[]
    for i in range(n_df):
        n.append(axe.bar(0, 0, color="gray", hatch=H * i))

    #l1 = axe.legend(h[::-1], l[::-1], loc='upper left', bbox_to_anchor=(0.02,1.1), ncol=4, fancybox=True, shadow=True)#n_col
    l1 = axe.legend(h[::-1], l[::-1], loc='upper right', ncol=1, bbox_to_anchor=(1.25,1), fancybox=True, shadow=True)#n_col
    if labels is not None:
        l2 = plt.legend(n, labels, loc='upper right')
    axe.add_artist(l1)
    return axe

# create fake dataframes
df1 = pd.DataFrame([
[1*0.7,57*0.7,47*0.7,27*0.7,5*0.7,0*0.7,15*0.7,0*0.7],
#[1*0.7,57*0.7,47*0.7,27*0.7,5*0.7,0.5*0.7,15*0.7,0.5*0.7],
#[1*0.7,57*0.7,47*0.7,27*0.7,5*0.7,1*0.7,17*0.7,1*0.7],
#[1*0.7,57*0.7,47*0.7,27*0.7,5*0.7,2*0.7,22*0.7,4*0.7],
[1*0.7,57*0.7,47*0.7,27*0.7,5*0.7,1*0.7,14*0.7,0.125*0.7],#1
[1*0.7,57*0.7,47*0.7,27*0.7,5*0.7,1*0.7,15*0.7,0.25*0.7],#2
[1*0.7,57*0.7,47*0.7,27*0.7,5*0.7,1*0.7,17*0.7,0.5*0.7],#4
[1*0.7,57*0.7,47*0.7,27*0.7,5*0.7,1*0.7,22*0.7,2*0.7],#8
[1*0.7,57*0.7,47*0.7,27*0.7,5*0.7,1*0.7,30*0.7,3.5*0.7]],#12
                   index=["B","TNT(1mm)","TNT(2mm)","TNT(4mm)","TNT(8mm)","TNT(12mm)"],
#                   columns=["SSR","Link", "Xbar","SA-G","SA-L","Buffer Rd","Buffer Wr","Clock"])
                   columns=["Clock","Buffer Wr", "Buffer Rd","Link","SA","Arbit","Xbar","Signal"])

# Then, just call :
plot_clustered_stacked([df1])
plt.axvline(x=0.5,color='k', linestyle='-',linewidth=3.0)
#plt.axvline(x=4.5,color='k', linestyle='-',linewidth=3.0)

plt.show()

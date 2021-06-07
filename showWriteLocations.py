import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

if __name__ == '__main__':
    irisdf = pd.read_csv('smallwritedeletef2fs.csv')
    # irisdf=irisdf[(irisdf['DISK'] == 'nvme0n1')]
    write = irisdf[(irisdf['T'] == 'W')]
    read = irisdf[(irisdf['T'] == 'R')]
    # ax = write.plot.scatter(x='TIME(s)', y = 'NormSector', c='color', label='write',s=2)
    # read.plot.scatter( ax=ax, x='TIME(s)', y = 'NormSector' ,label='read',s=2)
    # ax=ax,
    first = write[write['TIME(s)'].between(0,128)]
    delete1 = read[read['TIME(s)'].between(0,128)]
    second = write[write['TIME(s)'].between(128,710)]
    delete2 = read[read['TIME(s)'].between(128,710)]
    # third = irisdf[irisdf['TIME(s)'].between(348,511)]
    # delete3 = irisdf[irisdf['TIME(s)'].between(511,520)]
    # fourth = irisdf[irisdf['TIME(s)'].between(520,683)]
    # delete4 = irisdf[irisdf['TIME(s)'].between(683,693)]
    # fifth = irisdf[irisdf['TIME(s)'].between(693,856)]
    # delete5 = irisdf[irisdf['TIME(s)'].between(856, 865)]
    # sixth = irisdf[irisdf['TIME(s)'].between(865, 1200)]

    ax = first.plot.scatter(x='TIME(s)', y = 'NormSector', color="green",s=2,label='Allocate W')
    delete1.plot.scatter(ax=ax, x='TIME(s)', y = 'NormSector', color="orange",s=2,label='Allocate R')
    second.plot.scatter(ax=ax,x='TIME(s)', y = 'NormSector', color="red",s=2,label='Write')
    delete2.plot.scatter(ax=ax,x='TIME(s)', y = 'NormSector', color="blue",s=2 ,label='Read')
    # third.plot.scatter(ax=ax,x='TIME(s)', y = 'NormSector', color="pink",s=2,label='Third')
    # delete3.plot.scatter(ax=ax,x='TIME(s)', y= 'NormSector', color="red",s=2,label='_nolegend_')
    # fourth.plot.scatter(ax=ax,x='TIME(s)', y= 'NormSector', color="purple",s=2,label='Fourth')
    # delete4.plot.scatter(ax=ax,x='TIME(s)', y= 'NormSector', color="red",s=2,label='_nolegend_')
    # fifth.plot.scatter(ax=ax,x='TIME(s)', y= 'NormSector', color="green",s=2,label='Fifth')
    # delete5.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="red", s=2,label='_nolegend_')
    # sixth.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="yellow", s=2, label='Fifth')

    ax.set_title('File server f2fs')
    ax.set_xlabel("Time in seconds")
    ax.set_ylabel("Sector")
    plt.show()
    # irisdf = pd.read_csv('randomfullwritef2fs.csv')
    #
    # read= irisdf[(irisdf['T'] == 'W').between(0,266)]
    # write = irisdf[(irisdf['T'] == 'R').between(0,266)]
    # # ax = write.plot.scatter(x='TIME(s)', y = 'NormSector', c='color', label='write',s=2)
    # # read.plot.scatter( ax=ax, x='TIME(s)', y = 'NormSector' ,label='read',s=2)
    # # ax=ax,
    # first = irisdf[irisdf['TIME(s)'].between(266, 3000)]
    # # delete1 = irisdf[irisdf['TIME(s)'].between(164, 171)]
    # # second = irisdf[irisdf['TIME(s)'].between(171, 338)]
    # # delete2 = irisdf[irisdf['TIME(s)'].between(338, 348)]
    # # third = irisdf[irisdf['TIME(s)'].between(348, 511)]
    # # delete3 = irisdf[irisdf['TIME(s)'].between(511, 520)]
    # # fourth = irisdf[irisdf['TIME(s)'].between(520, 683)]
    # # delete4 = irisdf[irisdf['TIME(s)'].between(683, 693)]
    # # fifth = irisdf[irisdf['TIME(s)'].between(693, 856)]
    # # delete5 = irisdf[irisdf['TIME(s)'].between(856, 865)]
    # # sixth = irisdf[irisdf['TIME(s)'].between(865, 1200)]
    #
    # ax = write.plot.scatter(x='TIME(s)', y='NormSector', color="blue", s=2, label='read')
    # read.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="red", s=2, label='write')
    # first.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="purple", s=2, label='randwrite')
    # # second.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="orange", s=2, label='Second')
    # # delete2.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="red", s=2, label='_nolegend_')
    # # third.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="pink", s=2, label='Third')
    # # delete3.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="red", s=2, label='_nolegend_')
    # # fourth.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="purple", s=2, label='Fourth')
    # # delete4.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="red", s=2, label='_nolegend_')
    # # fifth.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="green", s=2, label='Fifth')
    # # delete5.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="red", s=2, label='_nolegend_')
    # # sixth.plot.scatter(ax=ax, x='TIME(s)', y='NormSector', color="yellow", s=2, label='Fifth')
    #
    # ax.set_title('Random write f2fs')
    # ax.set_xlabel("Time in seconds")
    # ax.set_ylabel("Sector")
    # plt.xlim([0, 200])
    # plt.ylim([0, 510000000])
    # plt.show()
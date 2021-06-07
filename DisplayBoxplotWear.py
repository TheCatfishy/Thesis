import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    outliers=dict(marker='o', markerfacecolor='red', markersize=5, markeredgecolor='none')
    write = pd.read_csv('smallwritedeleteext4loc.csv')
    print('loaded ext4 csv')
    freqCount = write.value_counts()
    print('counted ext4')
    write=None
    write2 = pd.read_csv('smallwritedeletef2fsloc.csv')
    print('loaded f2fs csv')
    freqCount2 = write2.value_counts()
    print('counted f2fs')
    write2=None
    print('combining')
    my_dict = {'ext4': freqCount, 'f2fs': freqCount2}
    print('plotting')
    fig, ax = plt.subplots()
    ax.boxplot(my_dict.values(), vert=False, flierprops=outliers)
    ax.set_title('Wear spread file server workload', fontsize=20,)
    ax.set_yticklabels(my_dict.keys())
    ax.set_xlabel("Write count in sectors",fontsize=10)
    print('show')
    plt.show()


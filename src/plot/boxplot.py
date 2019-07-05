#!/usr/bin/python3

## 箱形图的绘制
import matplotlib.pyplot as plt
import numpy as np

def boxplot(x_data,y_data,base_color='#539caf',median_color='#297083',
            x_label='',y_label='',title=''):

            _,ax = plt.subplots()
            ax.boxplot(y_data,
                        patch_artist = True,
                        medianprops = {'color': median_color},
                        boxprops = {'color': base_color, 'facecolor': base_color},
                        whiskerprops = {'color': base_color},
                        capprops = {'color': base_color})
            ax.set_xticklabels(x_data)
            ax.set_ylabel(y_label)
            ax.set_xlabel(x_label)
            ax.set_title(title)
            
"""
Author: Stergios Mekras
Email: stergios.mekras@gmail.com
"""

import tkinter as tk

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class RadarGraph(object):
    def __init__(self, container, source):
        self.container = container
        self.source = source

    def draw_graph(self):
        data_frame = pd.DataFrame(self.source, index=[0])
        labels = data_frame.keys()
        stats = data_frame.loc[0, labels].values
        number = len(labels)
        angles = np.linspace(0, 2 * np.pi, number, endpoint=False)
        stats = np.concatenate((stats, [stats[0]]))
        angles = np.concatenate((angles, [angles[0]]))
        if number > 5:
            colors = ['royalblue', 'brown', 'seagreen']
        else:
            colors = ['#750075', '#007500', '#000075', '#757500', '#750000']

        fig = plt.figure(figsize=(2, 2), facecolor='#F6F4F2', constrained_layout=True)

        ax = fig.add_subplot(111, polar=True)

        ax.set_facecolor('#F6F4F2')
        ax.set_yticklabels([])
        ax.set_theta_zero_location('E', offset=90)
        ax.tick_params(labelsize=0, pad=-17)
        if len(colors) > 3:
            for i in range(number):
                ax.bar(0.62 + angles[i], stats[i], color=colors[i], width=(2 * np.pi / number))
        else:
            for i in [0, 7]:
                ax.bar(0.4 + angles[i], stats[i], color=colors[0], width=(2 * np.pi / number))
            for i in [1, 2, 3]:
                ax.bar(0.4 + angles[i], stats[i], color=colors[1], width=(2 * np.pi / number))
            for i in [4, 5, 6]:
                ax.bar(0.4 + angles[i], stats[i], color=colors[2], width=(2 * np.pi / number))

        ax.fill_between(np.linspace(0, 2 * np.pi), 0, 1, color='#000000', alpha=0.5)
        ax.fill_between(np.linspace(0, 2 * np.pi), 1, 2, color='#111111', alpha=0.5)
        ax.fill_between(np.linspace(0, 2 * np.pi), 2, 3, color='#222222', alpha=0.5)
        ax.fill_between(np.linspace(0, 2 * np.pi), 3, 4, color='#333333', alpha=0.5)
        ax.fill_between(np.linspace(0, 2 * np.pi), 4, 5, color='#444444', alpha=0.5)
        ax.fill_between(np.linspace(0, 2 * np.pi), 5, 6, color='#555555', alpha=0.5)
        ax.fill_between(np.linspace(0, 2 * np.pi), 6, 7, color='#666666', alpha=0.5)
        ax.fill_between(np.linspace(0, 2 * np.pi), 7, 8, color='#777777', alpha=0.5)
        ax.fill_between(np.linspace(0, 2 * np.pi), 8, 9, color='#888888', alpha=0.5)
        ax.fill_between(np.linspace(0, 2 * np.pi), 9, 10, color='#999999', alpha=0.5)

        plt.xticks(angles, stats)
        if all(i <= 5 for i in stats):
            plt.ylim(0, 5)
        else:
            plt.ylim(0, 10)

        return fig

    def place_canvas(self, options=None):
        if options is None:
            options = []
        fig = self.draw_graph()
        canvas = FigureCanvasTkAgg(fig, self.container)
        canvas.draw()
        if options:
            canvas.get_tk_widget().grid(row=options[0], column=options[1], rowspan=options[2], columnspan=options[3])
        else:
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)

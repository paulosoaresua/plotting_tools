from typing import Any, List

import matplotlib.pyplot as plt


def add_legend_visibility_toggling(fig: Any, axs: List[Any], legend_location: str = "upper right"):
    series_to_legend_dict = {}
    for ax in axs:
        series = ax.get_lines()
        legend = ax.legend(loc=legend_location)

        for i, legend_series in enumerate(legend.get_lines()):
            legend_series.set_picker(True)
            legend_series.set_pickradius(10)
            series_to_legend_dict[legend_series] = series[i]

    def on_pick(event):
        legend_artist = event.artist
        is_visible = legend_artist.get_visible()

        series_to_legend_dict[legend_artist].set_visible(not is_visible)
        legend_artist.set_visible(not is_visible)

        fig.canvas.draw()

    plt.connect('pick_event', on_pick)

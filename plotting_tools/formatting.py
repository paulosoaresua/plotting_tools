from typing import Union

from enum import Enum


class CustomWidth(Enum):
    THESIS = "thesis"
    RESEARCH_NOTEBOOK = "research_notebook"


def calculate_best_figure_dimensions(width: Union[CustomWidth, float], fraction=1, subplots=(1, 1)):
    """Set figure dimensions to avoid scaling in LaTeX.
    From: https://jwalton.info/Embed-Publication-Matplotlib-Latex/

    Parameters
    ----------
    width: Union[str, float]
            Document textwidth or columnwidth in pts. Predefined strings are also acceptable.
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy
    subplots: array-like, optional
            The number of rows and columns of subplots.

    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    if isinstance(width, CustomWidth):
        # The widthts below were retrieved from proper latex files with the command: \showthe\textwidth
        if width == CustomWidth.THESIS:
            width_pt = 433.62
        elif width == CustomWidth.RESEARCH_NOTEBOOK:
            width_pt = 304.44
        else:
            raise Exception(f"Width not supported {width.}")
    else:
        width_pt = width

    # Width of figure (in pts)
    fig_width_pt = width_pt * fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    # https://disq.us/p/2940ij3
    golden_ratio = (5 ** .5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt

    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

    return fig_width_in, fig_height_in

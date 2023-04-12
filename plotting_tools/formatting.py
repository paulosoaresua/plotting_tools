from typing import Union

# The widths below were retrieved from proper latex files with the command: \showthe\textwidth
WIDTH_DICT = {
    "thesis": 433.62,
    "research_notebook": 433.62,
    "neurips": 397.48,
}


def calculate_best_figure_dimensions(document_width: Union[str, float], fraction=1, subplots=(1, 1)):
    """Set figure dimensions to avoid scaling in LaTeX.
    From: https://jwalton.info/Embed-Publication-Matplotlib-Latex/

    Parameters
    ----------
    document_width: Union[str, float]
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
    if isinstance(document_width, str):
        width_pt = WIDTH_DICT.get(document_width, None)
        if width_pt is None:
            raise Exception(f"Width {document_width} not supported. Available custom widths are {WIDTH_DICT}")
    else:
        width_pt = document_width

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

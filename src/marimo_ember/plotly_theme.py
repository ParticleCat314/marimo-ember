"""Plotly template matching ember.css. Requires plotly (`pip install marimo-ember[plotly]`).

    from marimo_ember.plotly_theme import PALETTE, style
    fig = px.line(df, x="date", y="close", color="symbol")
    style(fig, height=360, yfmt=".0%")

Importing this module registers the "ember" template and makes it plotly's default.
"""

from __future__ import annotations

import plotly.graph_objects as go
import plotly.io as pio

from marimo_ember import PALETTE

INK = "#f3e9dc"
INK_2 = "#c9b9a6"
INK_3 = "#8f8070"
GRID = "rgba(201, 185, 166, 0.10)"
SURFACE = "#201b17"

pio.templates["ember"] = go.layout.Template(
    layout=dict(
        colorway=PALETTE,
        paper_bgcolor="rgba(0,0,0,0)",  # let the marimo cell surface show through
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, ui-sans-serif, system-ui, sans-serif", color=INK_2, size=12),
        title=dict(font=dict(color=INK, size=15), x=0, xanchor="left"),
        margin=dict(l=12, r=12, t=36, b=12),
        hovermode="x unified",
        hoverlabel=dict(bgcolor="#2a231e", bordercolor="#574a3f", font=dict(color=INK, family="Inter, sans-serif")),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0, title_text="", font=dict(color=INK_2)),
        xaxis=dict(automargin=True, showgrid=False, linecolor="#3a3029", tickcolor="#3a3029", ticks="outside", tickfont=dict(color=INK_3), title=dict(text=None), zeroline=False),
        yaxis=dict(automargin=True, gridcolor=GRID, zeroline=False, linecolor="rgba(0,0,0,0)", tickfont=dict(color=INK_3), title=dict(font=dict(color=INK_2))),
        colorscale=dict(
            sequential=[[0, "#2a1a10"], [0.5, "#c2551c"], [1, "#ffd08a"]],
            diverging=[[0, "#3d95f0"], [0.5, "#4b3f35"], [1, "#f15e18"]],
        ),
    ),
    data=dict(scatter=[go.Scatter(line=dict(width=2))], scattergl=[go.Scattergl(line=dict(width=2))]),
)
pio.templates.default = "ember"


def style(fig: go.Figure, height: int = 360, yfmt: str | None = None) -> go.Figure:
    """Per-figure tweaks on top of the template: height and y tick format (e.g. '.0%')."""
    fig.update_layout(template="ember", height=height, xaxis_title=None, legend_title_text=None)
    if yfmt:
        fig.update_yaxes(tickformat=yfmt, hoverformat=yfmt.replace(".0", ".1"))
    return fig

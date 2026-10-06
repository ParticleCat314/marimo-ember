"""Ember: a warm dark theme for marimo, plus a matching Plotly template (marimo_ember.plotly_theme)."""

from __future__ import annotations

from pathlib import Path

__version__ = "0.1.0"
__all__ = ["PALETTE", "css_path"]

# Categorical slots in fixed order: blue, orange, teal, amber, pink, green, violet, red.
# Validated against the theme surfaces #201b17 and #171310: lightness band, chroma,
# colour-vision-deficiency separation and 3:1 contrast all pass.
PALETTE = ["#3d95f0", "#f15e18", "#09ad87", "#c38605", "#f54592", "#4dad1e", "#997bf4", "#ff4646"]


def css_path() -> Path:
    """Path of the bundled ember.css."""
    return Path(__file__).with_name("ember.css")

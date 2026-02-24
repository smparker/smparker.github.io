# Simulation Usability Improvements

General-purpose improvements for interactive spectrum simulators. These were developed for an HCl rotational spectrum but apply to any similar simulation.

## Replace CanvasJS with Plotly.js

CanvasJS is a paid library that displays "trial version" watermarks. Replace it with Plotly.js (MIT license, free, no watermarks).

- Use `<script src="https://cdn.plot.ly/plotly-2.35.2.min.js">` (or latest version)
- Data format: Plotly uses separate x and y arrays rather than `[{x, y}]` objects
- Use `Plotly.restyle()` to update data and `Plotly.relayout()` to update axes/layout without full redraws
- Set `responsive: true` in config for mobile-friendly resizing
- Set `displaylogo: false` and remove unnecessary mode bar buttons (`lasso2d`, `select2d`)

## Compute spectrum from parameters, not hardcoded data

Instead of embedding a giant JSON blob of precomputed frequencies and intensities, compute the spectrum from molecular constants. This makes it easy to add interactive controls that recompute on the fly (like the temperature slider below).

Precompute anything that doesn't depend on user-adjustable parameters (grid points, noise baseline) so that interactive updates only recompute what's necessary.

## Interactive temperature slider

Add a range slider that recomputes and redraws the spectrum live as the user drags it.

- Extract spectrum computation into a function that takes temperature as input
- Generate noise once at startup and reuse it, so the baseline doesn't jitter when the slider moves
- Use `Plotly.restyle()` to update just the y-data (fast, no full redraw)
- Still support a URL parameter (`?T=<value>`) to set the initial temperature, useful for linking to specific conditions

## Axis constraints

Enforce sensible axis behavior during zoom and pan:

- Keep zero at the bottom of the y-axis: listen for `plotly_relayout` events and reset `yaxis.range[0]` to 0 if the user pans it above zero
- Clamp x-axis panning to the data range so students can't scroll into empty space
- Combine both checks in a single `plotly_relayout` handler to avoid redundant relayout calls

## Log scale toggle

Add a checkbox to switch the y-axis between linear and log scale. This lets students see weak features (high-J lines, isotopologue shoulders) that are invisible on a linear scale. Implementation is a single `Plotly.relayout()` call toggling `yaxis.type` between `"linear"` and `"log"`.

## Peak picker (click-to-collect frequencies)

Let students click on peaks to build a running list of frequencies they can copy into a spreadsheet.

- Listen for `plotly_click` events on the chart div
- Store clicked x-values internally in a canonical unit, convert for display based on current unit selection
- Display as a numbered table below the chart
- Each row has an x button to remove individual entries
- "Copy" button writes all values (one per line, suitable for pasting into a spreadsheet column) to the clipboard via `navigator.clipboard.writeText()`
- "Clear" button resets the list
- Scrollable container (`max-height` with `overflow-y: auto`) so a long list doesn't push the page layout around

## Reduce point count for mobile performance

The original used 500k points; even 100k is more than needed. With a 400 cm⁻¹ range and 0.5 cm⁻¹ line width, 20k points (0.02 cm⁻¹ resolution) is visually identical and much more responsive on phones. Choose the minimum point count where the lines still look smooth — typically grid spacing should be ~1/25 of the narrowest line width.

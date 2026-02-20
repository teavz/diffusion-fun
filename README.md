# diffusion-fun

Fun with diffusion things for Cody SP26 Hack Week!

This repo contains:
- A Jupyter notebook (`extremediffusionfun.ipynb`) that generates images.
- A minimal, no-build React gallery (`frontend/react/index.html`) that displays results from `notebook_outputs/manifest.json/images`.

## Quick Start

1) Create and activate a virtual environment (optional but recommended)
- macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
- Windows (PowerShell): `py -m venv .venv; .\.venv\\Scripts\\Activate.ps1`

2) Install Jupyter (only needed to run the notebook)
- `pip install -U pip jupyter`

3) Run the notebook (to reproduce outputs)
- Launch: `jupyter lab` (or `jupyter notebook`)
- Open `extremediffusionfun.ipynb` and run all cells.

## View the Gallery (no build tools)

The frontend is a single static HTML file that uses React via CDN.
Open `frontend/react/index.html` in your browser.

## Project Layout

```
extremediffusionfun.ipynb
frontend/
  react/
    index.html
notebook_outputs/
  manifest.json/
    images/
      1.0/ 1.3/ 1.4/ 1.5/ 1.6/ 1.7/ 1.7.1/ 1.7.2/ 1.7.3/ 1.8/ 1.10/
```

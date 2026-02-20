# diffusion-fun

Fun with diffusion things for Cody SP26 Hack Week!

This repo contains:
- A Jupyter notebook (`extremediffusionfun.ipynb`) that generates images.
- A minimal, no-build React gallery (`frontend/react/index.html`) that displays results from `notebook_outputs/manifest.json/images`.

If you already have images in `notebook_outputs/manifest.json/images`, you can skip straight to “View the Gallery”.

## Quick Start

1) Create and activate a virtual environment (optional but recommended)
- macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
- Windows (PowerShell): `py -m venv .venv; .\\.venv\\Scripts\\Activate.ps1`

2) Install dependencies (only needed to run the notebook)
- `pip install -U pip jupyter python-dotenv huggingface_hub`

3) Configure your Hugging Face token (required for gated models/datasets)
- Copy `.env.example` to `.env` and paste your token:
  - `cp .env.example .env`
  - Edit `.env` and set `HUGGINGFACE_HUB_TOKEN=hf_...`
- Never commit `.env`. The canonical variable is `HUGGINGFACE_HUB_TOKEN`; `HF_TOKEN` is also supported.

4) Run the notebook (to reproduce outputs)
- Launch: `jupyter lab` (or `jupyter notebook`)
- Open `extremediffusionfun.ipynb` and run the cells.
- Near the top of the notebook, add this snippet to load your token:

```python
from notebooks_token_helper import setup_hf_token
setup_hf_token(verbose=True)
```

- The notebook saves images into `notebook_outputs/manifest.json/images/` in subfolders named for each section (e.g., `1.0`, `1.3`, …).

## View the Gallery (no build tools)

The frontend is a single static HTML file that uses React via CDN.

Option A — Open directly
- Open `frontend/react/index.html` in your browser.

Option B — Serve locally (recommended for consistent relative paths)
- From the repo root: `python3 -m http.server`
- Then open: `http://localhost:8000/frontend/react/index.html`

The page will render the following sections from `notebook_outputs/manifest.json/images`:
- 1.0 — model samples (manhat, rocketship, snowyvillage)
- 1.3 — one step denoising (t250a–c, t500a–c, t750a–c) with labels
- 1.4 — iterative denoising (a–f, blur)
- 1.5 — diffusion model sampling (a–e)
- 1.6 — classifier free guidance (a–e)
- 1.7 — image-to-image translation (rows: amalfi1–6, barista1–6, high1–6) with labels
- 1.7.1 — hand-drawn and web images (rows: avo1–6, lizard1–6) with labels
- 1.7.2 — mask (mask1–6)
- 1.7.3 — text conditioned image to image (rows: man1–6, pencil1–6, rocket1–6) with labels
- 1.8 — visual anagrams (manfire1–7)
- 1.10 — hybrid images (waterskull1–7)

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

## Submitting

- Ensure your generated images reside under `notebook_outputs/manifest.json/images` in the folder names above.
- Verify the gallery renders by opening `frontend/react/index.html` (or via the local server route).
- Do not commit your real Hugging Face token; `.env` should remain local.
- Include this README and the notebook in your submission.


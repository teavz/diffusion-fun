# diffusion-fun

Fun with diffusion things for Cody SP26 Hack Week!

This repo contains:
- A Jupyter notebook (`extremediffusionfun.ipynb`) that generates images.
- A minimal, no-build React gallery (`frontend/react/index.html`) that displays results from `notebook_outputs/manifest.json/images`.

## Quick Start

1) Install dependencies 
- `pip install -U pip jupyter python-dotenv huggingface_hub`

2) Configure your Hugging Face token
- Copy `.env.example` to `.env` and paste your token:
  - `cp .env.example .env`
  - Edit `.env` and set `HUGGINGFACE_HUB_TOKEN=hf_...`

3 Run the notebook (to reproduce outputs)
- Launch: `jupyter lab` (or `jupyter notebook`)
- Open `extremediffusionfun.ipynb` and run the cells.
- Near the top of the notebook, add this snippet to load your token:

```python
from notebooks_token_helper import setup_hf_token
setup_hf_token(verbose=True)
```

## View the Gallery (no build tools)

The frontend is a single static HTML file that uses React.

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


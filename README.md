# Python Compressive Sensing Demo

This repository demonstrates a simple compressed-sensing pipeline in pure Python:
1. **acquire.py**: subsamples a signal/image via random measurements.
2. **reconstruct.py**: recovers the original via L1-minimization or OMP.
3. **evaluate.py**: computes reconstruction error metrics (MSE, PSNR).
4. **demo script**: runs the full pipeline and saves comparison plots under `/figures`.

## Getting Started

```bash
# activate your virtual environment
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run a quick demo
python src/demo.py --input path/to/image.png --m 500


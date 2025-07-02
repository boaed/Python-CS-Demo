#!/usr/bin/env python3
"""
acquire.py


Subsample an image via random linear measurements.
"""


import argparse
import numpy as np
from PIL import Image


def parse_args():
    p = argparse.ArgumentParser(description="Acquire random measurements from an image")    
    p.add_argument("--input", "-i", required=True, help="Path to input image (grayscale)")
    p.add_argument("--m", "-m",type = int, required = True, help ="Number of measurements")
    p.add_argument("--output", "-o", default = "measurements.npz", help = "Output file for measurements (Numpy .npz)")
    
    return p.parse_args()

def load_image_gray(path):
    img = Image.open(path).convert("L")
    arr = np.array(img, dtype = np.float32) / 255.0
    
    return arr

def acquire_measurements(x,m):
    n = x.size
    Phi = np.random.randn(m,n) / np.sqrt(m)
    y = Phi.dot(x)

    return y, Phi

def main():
    args = parse_args()
    img = load_image_gray(args.input)
    x = img.flatten()
    y , Phi = acquire_measurements(x, args.m)
    np.savez(args.output, y= y, Phi = Phi, shape = img.shape)

    print(f"Saved {args.m} measurements to '{args.output}'.")


if __name__ == "__main__":
    main()

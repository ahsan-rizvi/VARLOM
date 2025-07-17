import scipy
import scipy.ndimage as nd
import matplotlib
from params import * # Import updated params
import params
import pandas as pd # For reading CSV for BTF/features

# Matplotlib backend for non-GUI environments
if params.device.type != 'cpu':
    matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import torch
from torch.utils import data
import os
import pathlib
import csv
import torch.nn.functional as F # Needed for BCE loss in train.py (was missing)


def SavePloat_Voxels(voxels_batch, path, iteration_prefix): # Renamed `voxels` to `voxels_batch` for clarity
    """
    Saves a batch of 3D voxel arrays as .npy files and plots their slices as .png.
    Assumes voxels_batch input is (N, D, H, W) where N is batch size.
    Each individual voxel volume will be (D, H, W).
    `iteration_prefix` can be an epoch number or filename base.
    """

# --- CustomImageDataset (Adapted for 3D MRI .npy files and Features from CSV/Numpy Array) ---
class CustomImageDataset(data.Dataset):
    def __init__(self, root_dir, feature_data=None): # Renamed feature_csv_path to feature_data for clarity
       
    def _match_images_and_features(self):
     
    def __getitem__(self, index):
   
    def __len__(self):
        return len(self.image_file_list)


# VARLOMS: A Multimodal CVAE Framework for Synthetic 3D MRI Generation from Multi-Omics Data

## Project Overview
An integrated pipeline for multi-omics and MRI data fusion using variational autoencoders. VARLOMS enables synthetic MRI generation from omics profiles and supports clinical prediction through a unified, interpretable framework.

## Data Description
The VARLOMS pipeline utilizes multi-omics datasets and corresponding MRI data. Omics data is preprocessed for normalization and feature selection, while MRI data is aligned and scaled for integration. The dataset includes paired samples enabling supervised learning for synthetic MRI generation and clinical prediction tasks.

## Code Description
The code used in this project is stored in a code directory and includes:
* main.py: Entry point for running the full VARLOMS pipeline.
* model.py: Defines the conditional variational autoencoder (VAE) architecture for omics-MRI integration.
* train.py: Handles model training, including data loading, loss computation, and optimization.
* test.py: Evaluates model performance on test datasets.
* funcs.py: Functions for metrics calculation and optional visualizations.
* params.py: Stores configuration parameters such as learning rate, batch size, paths, and model hyperparameters.

## File Structure
The file structure of the repository is as follows:
```.
├── data/
│   ├── Lateral_MRI/             # MEIs in .npy format
│   ├── Mutation.csv             # Mutation data
│   ├── Gistic2_CopyNumber.csv
│   ├── meta.csv
│   ├── HiSeqV2_mRNA.csv
│   ├── Methylation450.csv
│   ├── miRNA_HiSeq.csv
│   ├── merged.tsv                # Merged File for all omics data
├── code/Generation/
│   ├── model.py           
│   ├── train.py          
│   ├── funcs.py          
│   ├── main.py          
│   └── test.py          
│   └── params.py          
├── code/Task/
│   ├── main.py          
├── README.md                # Project overview and instructions
└── requirements.txt         # Python dependencies
```

## Installation
1. Prerequisites
Make sure you have following libraries installed.
* pandas==1.4.4
* numpy==1.21.5
* torch==1.12.1+cu116
* torchvision==0.13.1
* torchsummary==1.5.1
* tqdm==4.54.1
* seaborn==0.12.0
* scikit-learn==1.2.2
* xarray==0.20.1
* matplotlib==3.5.2
* tensorboardX==2.5.1
* pytorch-ignite==0.4.10
* pytorch-fid==0.3.0

You can install the dependencies by running:
```bash
pip3 install -r requirements.txt
```
2. Run

To run the model, execute the code/Task/main.py script. You can customize training parameters such as the number of epochs, learning rate, and other hyperparameters.

```bash
python3 code/Task/main.py 
```
3. For MRI Generation

To generate synthetic MRIs, execute the code/Generate/main.py script. You can customize training parameters such as the number of epochs, learning rate, and other hyperparameters.

```bash
python3 code/Generate/main.py
```

## Contact
Dr Ahsan Z Rizvi, ahsan.rizvi@iar.ac.in

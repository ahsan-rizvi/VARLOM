import torch

# --- Device Configuration ---
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# --- Global Training Parameters ---
batch_size =  # Original paper's batch size for 3D data. Increase if GPU allows.
model_save_step =  # Save checkpoints every X epochs

# --- Autoencoder (Feature Extraction) Parameters ---
# This AE will now process 3D MRI data and extract 'ae_latent_dim' features.
ae_epochs =  # Epochs for Autoencoder training
ae_lr =  # Learning rate for Autoencoder
ae_latent_dim =  # Number of latent features the Autoencoder extracts (matches BTF output)

# --- Conditional Variational Autoencoder (CVAE) Parameters ---
# This CVAE will generate 3D MRI data conditioned on 'ae_latent_dim' features.
cvae_epochs =  # Epochs for CVAE training
vae_lr =  # Learning rate for CVAE
cvae_latent_dim = # Internal latent dimension of the CVAE's 'z' space

# --- Image/Voxel Specific Parameters ---
cube_len =  # Original MRI voxel dimension (Y, X)
depth_len =  # Original MRI voxel dimension (Z)
leak_value =  # For LeakyReLU activation
bias =  # Use bias in conv layers or not

# --- Data and Model Directory Paths ---
# IMPORTANT: Update these paths to point to your actual data
data_dir = '../Lateral_MRI/' # Directory containing your .npy MRI files
omic_dir = '../merged.csv' # Path to your BTF features CSV file
test_dir= '../merged_test.csv' # Path to your test BTF features CSV file (for evaluation)
model_dir = 'trained_models/' # Directory to save AE and CVAE models (will be created under root)
output_dir = '../outputs/' # General output directory for generated images, logs
images_dir = '../test_outputs/' # Directory for test image generations
visualized = '../visualization/' # Directory for visualization outputs

# --- Control Flags for Training Stages ---
train_autoencoder =  # Set to True to train the AE to get features
train_cvae =  # Set to True to train the CVAE using AE features
evaluate_cvae_generation =  # Set to True to run the tester after training

def print_params():
    l = 16
   
    print(l * '*' + 'hyper-parameters' + l * '*')


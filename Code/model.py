import torch
import torch.nn as nn
import params # Import updated params, make sure params.py is also updated

class Conv3dBlock(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride=2, padding=1, bias=False, transpose=False, activation='leakyrelu'):
  
    def forward(self, x):
        return self.act(self.bn(self.conv(x)))

class AutoencoderEncoder(nn.Module):
    def __init__(self, ae_latent_dim):
     
    def forward(self, x):
      
        return latent_features

class AutoencoderDecoder(nn.Module):
    def __init__(self, ae_latent_dim):
  
    def forward(self, x):
      
        return reconstructed_image

class Autoencoder(nn.Module):
    def __init__(self, ae_latent_dim):
    
    def forward(self, x):
     
        return reconstructed, latent # Return both reconstructed image and latent features

class CVAE_Encoder(nn.Module):
    def __init__(self, cvae_latent_dim, num_conditional_features):
       
    def forward(self, image, conditional_features):
      
        return z_mean, z_log_var

class CVAE_Decoder(nn.Module):
    def __init__(self, cvae_latent_dim, num_conditional_features):
    
    def forward(self, z, conditional_features):
       
        return decoded_image

class CVAE(nn.Module):
    def __init__(self, cvae_latent_dim, num_conditional_features):
     
    def encode(self, image, conditional_features):
        return self.encoder(image, conditional_features)

    def decode_and_generate(self, z, conditional_features):
        return self.decoder(z, conditional_features)

    def decode(self, z, conditional_features):
        return self.decoder(z, conditional_features)

    def reparameterize(self, mu, logvar):
        return mu + eps * std # Reparameterization formula

    def forward(self, image, conditional_features):
      
        return reconstructed_image, mu, logvar


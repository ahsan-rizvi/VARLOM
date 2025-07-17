import argparse
from train import trainer_main 
from test import tester 
import torch 
import params 

def str2bool(v):

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--logs', type=str, default='autoencoder_cvae_run', help='logs by tensorboardX, and sub-directory for models/outputs')
    parser.add_argument('--model_name', type=str, default="ae_cvae", help='model name for saving (e.g., ae_cvae)')
    parser.add_argument('--test', type=str2bool, default=False, help='Set to True to run testing/generation phase')

    args = parser.parse_args()
    params.print_params()
    if not args.test:
        print("\n--- Initiating Training Pipeline (Autoencoder + CVAE) ---")
        trainer_main(args) # Call our new orchestrating trainer
    else:
        print("\n--- Initiating Testing/Generation Pipeline (CVAE) ---")
        tester(args) 

    print("\nProgram finished.")

if __name__ == '__main__':
    main()


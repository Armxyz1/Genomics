import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_distribution(save_path):
    df = pd.read_csv(f"{save_path}/processed_reads.csv")

    df = df[df['pos'].str.lower() != 'nil']  # Keep rows where 'pos' is not 'Nil'
    df['pos'] = df['pos'].astype(int)  # Convert 'pos' to integer
    
    # Plotting a histogram of the read start positions
    plt.figure(figsize=(12, 6))
    plt.hist(df['pos'], bins=100, color='skyblue', edgecolor='black')  # Adjust 'bins' as needed for granularity
    
    # Adding labels and title
    plt.xlabel('Position on Reference Sequence')
    plt.ylabel('Frequency of Read Start Positions')
    plt.title('Distribution of Read Start Positions on the Reference Sequence')
    plt.savefig(f"{save_path}/read_distribution.png")

def coverage(save_path, reference, bwt, map):
    df = pd.read_csv(f"{save_path}/processed_reads.csv")
    
     

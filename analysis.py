import pandas as pd
import numpy as np
from model import ForestFireModel

def run_simulation(steps=150, wind=(1,0), humidity=None, filename="results.csv"):
    
    model = ForestFireModel(size=100, wind=wind, fixed_humidity=humidity)
    
    data = []
    
    for t in range(steps):
        burning = np.sum(model.grid == 2)
        burned = np.sum(model.grid == 3)
        trees = np.sum(model.grid == 1)
        
        data.append([t, burning, burned, trees])
        
        model.step()
        
        if burning == 0:
            break
    
    df = pd.DataFrame(data, columns=["time", "burning", "burned", "trees"])
    df.to_csv(filename, index=False)
    
    print(f"Saved results to {filename}")


import matplotlib.pyplot as plt

def plot_comparison(file1, file2, label1="No Wind", label2="Wind"):
    plt.yscale("log")

    plt.ylim(0, 50)

    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    plt.figure(figsize=(8,6))
    
    plt.plot(df1["time"], df1["burned"], label=label1)
    plt.plot(df2["time"], df2["burned"], label=label2)
    
    plt.xlabel("Time Step")
    plt.ylabel("Burned Area (cells)")
    plt.title("Comparison of Burned Area Over Time")
    plt.legend()
    
    plt.savefig("comparison_plot.png", dpi=300)
    plt.show()

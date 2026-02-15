import pandas as pd
import numpy as np
from model import ForestFireModel

def run_simulation(steps=150, wind=(1,0), filename="results.csv"):
    
    model = ForestFireModel(size=100, wind=wind)
    
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

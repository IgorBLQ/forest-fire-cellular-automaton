import numpy as np

EMPTY = 0
TREE = 1
BURNING = 2
BURNED = 3

class ForestFireModel:
    def __init__(self, size=100, tree_density=0.7, base_prob=0.3):
        self.size = size
        self.tree_density = tree_density
        self.base_prob = base_prob
        
        self.grid = self.initialize_grid()
        self.humidity = np.random.rand(size, size)
        
    def initialize_grid(self):
        grid = np.random.choice(
            [EMPTY, TREE],
            size=(self.size, self.size),
            p=[1 - self.tree_density, self.tree_density]
        )
        
        # Ignite center
        center = self.size // 2
        grid[center, center] = BURNING
        return grid

    def count_burning_neighbors(self, i, j):
        neighbors = self.grid[i-1:i+2, j-1:j+2]
        return np.sum(neighbors == BURNING)

    def step(self):
        new_grid = self.grid.copy()
        
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                
                if self.grid[i, j] == TREE:
                    burning_neighbors = self.count_burning_neighbors(i, j)
                    
                    if burning_neighbors > 0:
                        p = 1 - (1 - self.base_prob)**burning_neighbors
                        p *= (1 - self.humidity[i, j])
                        
                        if np.random.rand() < p:
                            new_grid[i, j] = BURNING
                            
                elif self.grid[i, j] == BURNING:
                    new_grid[i, j] = BURNED
                    
        self.grid = new_grid

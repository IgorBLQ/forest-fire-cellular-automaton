import numpy as np

EMPTY = 0
TREE = 1
BURNING = 2
BURNED = 3

class ForestFireModel:
    def __init__(self, size=100, tree_density=0.7, base_prob=0.3,
                 wind=(1,0), wind_strength=0.5,
                 fixed_humidity=None):

        self.size = size
        self.tree_density = tree_density
        self.base_prob = base_prob
        
        self.wind = np.array(wind)
        if np.linalg.norm(self.wind) != 0:
            self.wind = self.wind / np.linalg.norm(self.wind)
        self.wind_strength = wind_strength
        
        self.grid = self.initialize_grid()
        
        if fixed_humidity is not None:
            self.humidity = np.full((size, size), fixed_humidity)
        else:
            self.humidity = np.random.rand(size, size)
        
    def initialize_grid(self):
        grid = np.random.choice(
            [EMPTY, TREE],
            size=(self.size, self.size),
            p=[1 - self.tree_density, self.tree_density]
        )
        
        center = self.size // 2
        grid[center, center] = BURNING
        return grid

    def step(self):
        new_grid = self.grid.copy()
        
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                
                if self.grid[i, j] == TREE:
                    ignition_probability = 0
                    
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            
                            if di == 0 and dj == 0:
                                continue
                                
                            ni, nj = i + di, j + dj
                            
                            if self.grid[ni, nj] == BURNING:
                                
                                direction = np.array([di, dj])
                                direction = direction / np.linalg.norm(direction)
                                
                                wind_factor = 1 + self.wind_strength * np.dot(self.wind, direction)
                                
                                local_p = self.base_prob * (1 - self.humidity[i, j]) * wind_factor
                                
                                ignition_probability = 1 - (1 - ignition_probability) * (1 - local_p)
                    
                    if np.random.rand() < ignition_probability:
                        new_grid[i, j] = BURNING
                        
                elif self.grid[i, j] == BURNING:
                    new_grid[i, j] = BURNED
                    
        self.grid = new_grid

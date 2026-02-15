# 🔥 Forest Fire Cellular Automaton  
### Probabilistic Modeling of Wildfire Propagation with Humidity and Wind

---

## 📌 Overview

This project implements a **probabilistic two-dimensional Cellular Automaton (CA)** to model wildfire propagation under varying environmental conditions.

The model incorporates:

- 🌬 Fixed directional wind (vector-based influence)  
- 💧 Variable humidity levels (probabilistic damping factor)  
- 🌲 Stochastic fire spread dynamics  
- 📊 Ensemble simulations with statistical analysis  

The objective is to investigate how **humidity affects wildfire propagation**, using a computational framework grounded in cellular automata theory.

The project culminates in a scientific-style article supported by reproducible simulations and statistical analysis.

---

## 🎯 Objectives

- Implement wildfire propagation using Cellular Automata  
- Introduce probabilistic ignition rules  
- Incorporate environmental factors (humidity and wind)  
- Perform ensemble simulations (30 runs per condition)  
- Compute statistical metrics (mean and standard deviation)  
- Generate publication-style figures  
- Ensure full reproducibility  

---

## 🧠 Theoretical Foundation

### Cellular Automaton Components

1. **Lattice**  
   A 2D grid (100 × 100) representing a forest.

2. **Cell States**
   - `0` → Empty  
   - `1` → Tree (unburned)  
   - `2` → Burning  
   - `3` → Burned  

3. **Neighborhood**  
   Moore neighborhood (8 adjacent cells).

4. **Transition Rule**  
   Probabilistic ignition influenced by:
   - Number of burning neighbors  
   - Humidity level  
   - Wind direction  

---

## 🔬 Mathematical Model

The ignition probability of a tree cell is modeled as:

P(i, t+1) = P_base × (1 − H) × (1 + α (V · d_ij))

Where:

- `P_base` → intrinsic propagation probability  
- `H ∈ [0,1]` → humidity level  
- `V` → wind vector  
- `d_ij` → direction from burning neighbor to cell  
- `α` → wind influence coefficient  

Interpretation:

- Higher humidity reduces ignition probability.  
- Wind aligned with propagation increases ignition probability.  
- Opposing wind reduces ignition probability.  

---

## 📊 Experimental Setup

- Grid size: `100 × 100`
- Initial tree density: `0.7`
- Wind vector: `(1, 0)` (constant horizontal wind)
- 30 independent simulations per humidity level
- Fixed random seed for reproducibility

### Humidity Levels Tested

- `H = 0.2` (Low humidity)
- `H = 0.5` (Intermediate humidity)
- `H = 0.8` (High humidity)

---

## 📈 Results

| Humidity | Mean Burned Area | Standard Deviation |
|----------|-----------------|-------------------|
| 0.2      | 15.47           | 19.50             |
| 0.5      | 4.50            | 4.16              |
| 0.8      | 1.43            | 0.92              |

### Observations

- Monotonic decrease in burned area as humidity increases.
- Higher stochastic variance at low humidity.
- Indication of near-critical behavior in low moisture regime.

Generated figure:

`humidity_analysis.png`

This figure displays mean burned area with error bars (standard deviation).

---

## 📁 Project Structure


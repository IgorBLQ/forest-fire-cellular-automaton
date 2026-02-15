🔥 Forest Fire Cellular Automaton
Probabilistic Modeling of Wildfire Propagation with Humidity and Wind
📌 Overview

This project implements a probabilistic two-dimensional Cellular Automaton (CA) to model wildfire propagation under varying environmental conditions.

The model incorporates:

🌬 Fixed directional wind (vector-based influence)

💧 Variable humidity levels (probabilistic damping factor)

🌲 Stochastic fire spread dynamics

📊 Ensemble simulations with statistical analysis

The objective is to investigate how humidity affects wildfire propagation, using a computational framework grounded in cellular automata theory.

The project culminates in a scientific-style article supported by reproducible simulations and statistical analysis.

🎯 Objectives

Implement wildfire propagation using Cellular Automata

Introduce probabilistic ignition rules

Incorporate environmental factors (humidity and wind)

Perform ensemble simulations (30 runs per condition)

Compute statistical metrics (mean and standard deviation)

Generate publication-style figures

Ensure full reproducibility

🧠 Theoretical Foundation
Cellular Automaton Components

Lattice
A 2D grid (100 × 100) representing a forest.

Cell States

0 → Empty

1 → Tree (unburned)

2 → Burning

3 → Burned

Neighborhood
Moore neighborhood (8 adjacent cells).

Transition Rule
Probabilistic ignition influenced by:

Number of burning neighbors

Humidity level

Wind direction

🔬 Mathematical Model

The ignition probability of a tree cell is modeled as:

P(i, t+1) = P_base × (1 − H) × (1 + α (V · d_ij))


Where:

P_base → intrinsic propagation probability

H ∈ [0,1] → humidity level

V → wind vector

d_ij → direction from burning neighbor to cell

α → wind influence coefficient

Interpretation:

Higher humidity reduces ignition probability.

Wind aligned with propagation increases ignition probability.

Opposing wind reduces ignition probability.

📊 Experimental Setup

Grid size: 100 × 100

Initial tree density: 0.7

Wind vector: (1, 0) (constant horizontal wind)

30 independent simulations per humidity level

Fixed random seed for reproducibility

Humidity Levels Tested

H = 0.2 (Low humidity)

H = 0.5 (Intermediate humidity)

H = 0.8 (High humidity)

📈 Results
Humidity	Mean Burned Area	Standard Deviation
0.2	15.47	19.50
0.5	4.50	4.16
0.8	1.43	0.92
Observations

Monotonic decrease in burned area as humidity increases.

Higher stochastic variance at low humidity.

Indication of near-critical behavior in low moisture regime.

Generated figure:

humidity_analysis.png


This figure displays mean burned area with error bars (standard deviation).

📁 Project Structure
cellular-automaton/
│
├── model.py                # Core cellular automaton implementation
├── analysis.py             # Supporting analysis tools
├── experiments.py          # Automated ensemble simulations
├── humidity_summary.csv    # Statistical results
├── humidity_analysis.png   # Generated figure
├── article.tex             # Scientific article (LaTeX)
└── README.md               # Project documentation

🚀 How to Run
1️⃣ Install Dependencies
pip install numpy pandas matplotlib

2️⃣ Run the Experiments
python experiments.py


This will automatically:

Run 30 simulations per humidity level

Compute mean and standard deviation

Generate humidity_summary.csv

Generate humidity_analysis.png

🔁 Reproducibility

The project uses:

np.random.seed(42)


This ensures reproducible results across different machines.

🧪 Scientific Contribution

This project demonstrates:

Emergent behavior from simple local probabilistic rules

Suppressive effect of humidity on wildfire propagation

Increased stochastic variability at low humidity

Applicability of Cellular Automata to environmental modeling

It highlights how discrete computational models can capture essential features of complex natural systems.

🤖 LLM-Assisted Research Workflow

An important aspect of this project was the structured use of a Large Language Model (LLM) as an intellectual assistant during development.

The LLM was used to:

Deepen theoretical understanding of Cellular Automata

Refine probabilistic modeling strategies

Formalize mathematical expressions

Improve LaTeX scientific writing

Validate statistical reasoning

Structure the article and documentation

The LLM acted as a research assistant — supporting conceptual clarity, not replacing critical reasoning.

This reflects a modern hybrid human–AI research workflow.

⚠️ Model Limitations

No terrain/topography modeling

Homogeneous fuel assumption

Fixed wind direction

Discrete space-time grid (possible anisotropy effects)

No real-world GIS data integration

🌍 Possible Extensions

Variable wind fields

Terrain slope modeling

Heterogeneous vegetation

Percolation threshold analysis

Phase transition study

Real satellite data integration

GPU acceleration for large-scale simulations

📄 Scientific Article

The full article is available in:

article.tex


Compile using:

pdflatex article.tex

⭐ Final Remarks

This project integrates:

Complex systems theory

Probabilistic modeling

Computational simulation

Statistical ensemble analysis

Scientific writing and documentation

AI-assisted research workflow

It demonstrates how simple rule-based systems can generate rich, emergent dynamics — reinforcing the power of Cellular Automata in modeling environmental propagation systems.
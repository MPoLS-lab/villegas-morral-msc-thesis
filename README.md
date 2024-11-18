# Agent-based modelling of embryonic organoid development

![Language: Julia](https://img.shields.io/badge/language-Julia-ed207b)
![Jupyter Notebook](https://img.shields.io/badge/Notebook-Jupyter-f37821)

**This model has been programmed using [CellBasedModels.jl](https://github.com/dsb-lab/CellBasedModels.jl), the Julia package for multicellular modelling.**


## Table of Contents

1. [Introduction](#introduction)
2. [Abstract](#abstract)
3. [Report outline](#report-outline)
4. [Code outline](#code-outline)
5. [Installation process](#installation-process)
6. [Poster](#poster)



## Introduction

<sup>[_Return to the Table of Contents_](#table-of-contents)</sup>

This repository contains the code, figures and report of the master thesis, titled "Agent-based modelling of embryonic organoid development", developed by [Víctor Villegas-Morral](https://github.com/villegas-morral) in 2024 as part of the Master's degree in Advanced Mathematics and Mathematical Engineering at Universitat Politècnica de Catalunya. It was carried out at the  Multiscale Physics of Living Systems Group, part of the Computational Biology and Complex Systems Research Group ([BIOCOM-SC](https://biocomsc.upc.edu/en)), and supervised by [David Oriola Santandreu](https://davidoriola.mystrikingly.com/). 



## Abstract

<sup>[_Return to the Table of Contents_](#table-of-contents)</sup>

In recent years, embryonic organoids have become an increasingly important tool for studying complex developmental processes that are difficult to access in actual animal embryos. These _in vitro_ structures can be generated in a high-throughput manner and have the advantage of mimicking many intricate behaviours observed in real embryos. In this study, we describe an agent-based model designed to simulate the development of embryonic organoids, and implement it using CellBasedModels.jl, the Julia package for multicellular modelling. Our model integrates mechanical interactions with cellular differentiation and accounts for the stochastic nature of both cell-cell interactions and cell fate transitions. We provide a comprehensive overview of the key simplifications made in the mathematical model and offer a numerical justification for these choices. Finally, we use the model to simulate the early stages of gastruloid formation, analysing the roles of cell differentiation and differential adhesion.



## Report outline

<sup>[_Return to the Table of Contents_](#table-of-contents)</sup>

The report is structured as follows.

0. **Nomenclature**
1. **Introduction**
2. **Agent-based modelling of 3D cellular aggregates**: mathematical description of the proliferation, mechanical interactions, cell differentiation, and nondimensionalization.
3. **Implementation of the model**: computational framework, numerical methods, and numerical validation of the approximations described previously.
4. **Test examples and applications**: physical description of a real-life experiment, and implementation and analysis of such experiment varying the model.
5. **Conclusions and further work**
6. **Appendix**: mathematical derivations, explanation of the programs, and additional figures.
7. **References**



## Code outline

<sup>[_Return to the Table of Contents_](#table-of-contents)</sup>

The programs referenced across the report. The following brief descriptions are provided in the Appendix.

- **Packages**: Loads the packages needed for the project.  
- **Model**: Loads the default model.  
- **Functions**: Loads most of the functions used by the programs.  
- **3.01**: Visualization of the issue regarding the increase of neighbours. Averaged over several realizations.  
- **3.02**: Analysis of the issue regarding the increase of neighbours.  
- **3.03**: Parameter sweep for `α_adh` using the variable friction model.  
- **3.04**: Parameter sweep for `α_adh` using the constant friction model.  
- **3.05**: Proposed model with constant friction.  
- **3.06**: Instability of the model using a simple force expression.  
- **3.07**: Computation of the sum of velocities of the neighbours using the model introduced in Program `3.03`.
- **4.00**: Example displaying the main features and functions of the code.  
- **4.01**: Loop that simulates communities using different parameters in order to perform parameter sweep and ensure stability.  
- **4.02**: Simulation assuming that proliferation continues during differentiation.  
- **4.03**: Measurement of the growth of cells.  
- **4.04**: Measurement of the effect of protrusions.  
- **4.05**: Average of the proportions of cell types for several realizations and comparison of the output to known solutions. It includes computations for several configurations.  
- **4.06**: Replica of the computations performed in Program `4.05` using the set-up described in Program `4.02`. 
- **4.07 and 4.08**: Computation of the proportion of cells in state B in terms of its initial proportion for a given set of timestamps, and comparison with known solutions. For a single realization in `4.07`, and averaged in `4.08`.  
- **4.09**: Simulation assuming that force between two cells can change depending on their states. Plots the cells in each state to visualise the effect.  
- **4.10**: Replica of the computations performed in Programs `4.05` and `4.08` using the set-up described in Program `4.09`.  
- **4.11**: Replica of the computations performed in Programs `4.05` using the set-up described in Program `4.09` along with proliferation during the differentiation process.
- **4.12**: Ideas for the implementation of a measure for polarization.
- **images2gif.py**: Python script that finds plots in the folder and converts them into a GIF.  



## Installation process

<sup>[_Return to the Table of Contents_](#table-of-contents)</sup>

The following instructions provide a guide to set up your computer to run the code, and been tested to work on Linux and Windows.

Download Julia from [their website](https://julialang.org/downloads/). Download version 1.9 and, optionally, set it as default and remove the release version.

```
juliaup add 1.9
juliaup default 1.9
juliaup rm release
```

Run Julia.
```
julia
```
In case 1.9 is not the default version, run
```
julia +1.9
```

Add CellBasedModels.jl and the packages used across the code
```julia-repl
julia> using Pkg
julia> add CellBasedModels
julia> add DifferentialEquations, Distributions, Random, GLMakie, Printf, Dates, Glob, NBInclude, MathTeXEngine, IJulia
```
Note that IJulia is only necessary to run the notebooks in Jupyter notebooks. You can use [JupyterLab](https://jupyter.org/install). Another option is to use VS Code along with the Julia extension.



## Poster

<sup>[_Return to the Table of Contents_](#table-of-contents)</sup>

# Agent-based modelling of embryonic organoid development

![Language: Julia](https://img.shields.io/badge/language-Julia-ed207b)
![Jupyter Notebook](https://img.shields.io/badge/Notebook-Jupyter-f37821)

**This model has been programmed using [CellBasedModels.jl](https://github.com/dsb-lab/CellBasedModels.jl), the Julia package for multicellular modelling.**


## Table of Contents

1. [Introduction](#introduction)
2. [Abstract](#abstract)
3. [Report outline](#report-outline)
4. [Code outline](#code-outline)
5. [Installation process](#installation-process)
6. [Poster](#poster)



## Introduction

<sup>[_Return to the Table of Contents_](#table-of-contents)</sup>

This repository contains the code, figures and report of my master thesis, titled "Agent-based modelling of embryonic organoid development", developed in 2024 as part of the Master's degree in Advanced Mathematics and Mathematical Engineering at Universitat Politècnica de Catalunya. It was carried out at the  Multiscale Physics of Living Systems Group, part of the Computational Biology and Complex Systems Research Group ([BIOCOM-SC](https://biocomsc.upc.edu/en)), and supervised by [David Oriola Santandreu](https://davidoriola.mystrikingly.com/). 



## Abstract

<sup>[_Return to the Table of Contents_](#table-of-contents)</sup>

In recent years, embryonic organoids have become an increasingly important tool for studying complex developmental processes that are difficult to access in actual animal embryos. These _in vitro_ structures can be generated in a high-throughput manner and have the advantage of mimicking many intricate behaviours observed in real embryos. In this study, we describe an agent-based model designed to simulate the development of embryonic organoids, and implement it using CellBasedModels.jl, the Julia package for multicellular modelling. Our model integrates mechanical interactions with cellular differentiation and accounts for the stochastic nature of both cell-cell interactions and cell fate transitions. We provide a comprehensive overview of the key simplifications made in the mathematical model and offer a numerical justification for these choices. Finally, we use the model to simulate the early stages of gastruloid formation, analysing the roles of cell differentiation and differential adhesion.



## Report outline

<sup>[_Return to the Table of Contents_](#table-of-contents)</sup>

The report is structured as follows.

0. **Nomenclature**
1. **Introduction**
2. **Agent-based modelling of 3D cellular aggregates**: mathematical description of the proliferation, mechanical interactions, cell differentiation, and nondimensionalization.
3. **Implementation of the model**: computational framework, numerical methods, and numerical validation of the approximations described previously.
4. **Test examples and applications**: physical description of a real-life experiment, and implementation and analysis of such experiment varying the model.
5. **Conclusions and further work**
6. **Appendix**: mathematical derivations, explanation of the programs, and additional figures.
7. **References**



## Code outline

<sup>[_Return to the Table of Contents_](#table-of-contents)</sup>

The programs referenced across the report. The following brief descriptions are provided in the Appendix.

- **Packages**: Loads the packages needed for the project.  
- **Model**: Loads the default model.  
- **Functions**: Loads most of the functions used by the programs.  
- **3.01**: Visualization of the issue regarding the increase of neighbours. Averaged over several realizations.  
- **3.02**: Analysis of the issue regarding the increase of neighbours.  
- **3.03**: Parameter sweep for `α_adh` using the variable friction model.  
- **3.04**: Parameter sweep for `α_adh` using the constant friction model.  
- **3.05**: Proposed model with constant friction.  
- **3.06**: Instability of the model using a simple force expression.  
- **3.07**: Computation of the sum of velocities of the neighbours using the model introduced in Program `3.03`.
- **4.00**: Example displaying the main features and functions of the code.  
- **4.01**: Loop that simulates communities using different parameters in order to perform parameter sweep and ensure stability.  
- **4.02**: Simulation assuming that proliferation continues during differentiation.  
- **4.03**: Measurement of the growth of cells.  
- **4.04**: Measurement of the effect of protrusions.  
- **4.05**: Average of the proportions of cell types for several realizations and comparison of the output to known solutions. It includes computations for several configurations.  
- **4.06**: Replica of the computations performed in Program `4.05` using the set-up described in Program `4.02`. 
- **4.07 and 4.08**: Computation of the proportion of cells in state B in terms of its initial proportion for a given set of timestamps, and comparison with known solutions. For a single realization in `4.07`, and averaged in `4.08`.  
- **4.09**: Simulation assuming that force between two cells can change depending on their states. Plots the cells in each state to visualise the effect.  
- **4.10**: Replica of the computations performed in Programs `4.05` and `4.08` using the set-up described in Program `4.09`.  
- **4.11**: Replica of the computations performed in Programs `4.05` using the set-up described in Program `4.09` along with proliferation during the differentiation process.
- **4.12**: Ideas for the implementation of a measure for polarization.
- **images2gif.py**: Python script that finds plots in the folder and converts them into a GIF.  



## Installation process

<sup>[_Return to the Table of Contents_](#table-of-contents)</sup>

The following instructions provide a guide to set up your computer to run the code, and been tested to work on Linux and Windows.

Download Julia from [their website](https://julialang.org/downloads/). Download version 1.9 and, optionally, set it as default and remove the release version.

```
juliaup add 1.9
juliaup default 1.9
juliaup rm release
```

Run Julia.
```
julia
```
In case 1.9 is not the default version, run
```
julia +1.9
```

Add CellBasedModels.jl and the packages used across the code
```julia-repl
julia> using Pkg
julia> add CellBasedModels
julia> add DifferentialEquations, Distributions, Random, GLMakie, Printf, Dates, Glob, NBInclude, MathTeXEngine, IJulia
```
Note that IJulia is only necessary to run the notebooks in Jupyter notebooks. You can use [JupyterLab](https://jupyter.org/install). Another option is to use VS Code along with the Julia extension.



## Poster

<sup>[_Return to the Table of Contents_](#table-of-contents)</sup>

Poster created for the 2024 Collaboratorium Annual Symposium ("Modelling Biology Across Scales").

![](https://github.com/MPoLS-lab/villegas-morral-msc-thesis/blob/809730a71c66272e6039178b0437279e55143d9e/report/poster.jpg)


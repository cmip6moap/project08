# Interactive graphics of key CMIP6-based IPCC figures

Figures in IPCC reports, especially those in the Summaries for Policy Makers, are often densely packed with information from multiple sources. This makes it challenging to understand the full impact of the figure without having additional information. This project will investigate adding interactive elements to key IPCC figures from the 5th Assessment Report or other recent Special Reports. These elements could include highlighting key aspects and relating them to key conclusions, adding numerical values or even animating graphics. The possibilities are endless.

## Contributors

* Lily Gouldsbrough, Lancaster Environment Centre, Lancaster University, Lancaster, UK, Twitter: https://twitter.com/lilygouldsbr
* Matt Amos, Lancaster Environment Centre, Lancaster University, Lancaster, UK, Twitter: https://twitter.com/mattamosphere
* Christoph Sauter, Department of Civil and Environmental Engineering, University of Strathclyde, Glasgow, UK
* Viola Heinrich, School of Geographical Sciences, University of Bristol, UK
* Ying Chen, University of Exeter
* Stephen Kelly, National Oceanography Centre, Southampton, UK
* Mat Collins, University of Exeter

## What was done
We created 3 interactive figures using CMIP6 data.
* Figure 1: Global changes in CO2 emissions [here](https://nbviewer.jupyter.org/github/cmip6moap/project08/blob/main/results/CO2_emissions.html)
* Figure 2: Regional Average Mean Changes in Temperature [here](https://htmlpreview.github.io/?https://github.com/cmip6moap/project08/blob/main/results/Mean_regional_surface_temperature_by_location.html) and [here](https://htmlpreview.github.io/?https://github.com/cmip6moap/project08/blob/main/results/Mean_regional_surface_temperature_by_ssp.html)
* Figure 3: Temperature Anamoly Relative to 1861-1890 Average [here](https://htmlpreview.github.io/?https://github.com/cmip6moap/project08/blob/main/results/temperature_changes_over_time.html)

### How we approached the problem and why

Initially, we spent time processing the data...

### Data we used and how to obtain this

* * AR6 region definitions https://github.com/SantanderMetGroup/ATLAS/tree/master/reference-regions
* * Historical and projected CO2 emissions data (https://esgf-node.llnl.gov/search/input4mips/)

### What we did during the hackathon

* Processed and analyised the respective data being used as the input to the interactive figures
* Used the AR6 region definitions that will be used in the IPCC 6th Assessment Report (AR6) we created an interactive map
* Created an interactive graph of global historical and future net carbon emissions under different Shared Socio-Econimic Pathways (SPPs)
* Created an interactive world map plot showing the temperature anomaly relative to 1861-1890 average using SSP3.70 Regional Rivalry

### Outcomes

* [...]
* [...]
* [...]

## About this repo

There are further `README` files in key directories.

### Key files

* [...]
* [...]
* [...]

### How to reproduce our outputs

1. [...]
2. [...]
3. [...]

### Repo structure

    .
    ├── notebooks
    │   ├── [...].ipynb
    │   └── [...].ipynb
    │           The Jupyter Notebooks that we created
    │
    ├── code
    │   ├── [...].py
    │   └── [...].py
    │           Any code (Python or otherwise) that we created that doesn't
    │           sit within a Notebook
    │
    ├── results
    │   ├── [...].pdf
    │   └── [...].png
    │           The key figures that we produced
    │
    ├── data
    │   ├── raw_data
    │   │       Any data we used that didn't come from JASMIN
    │   │
    │   └── processed_data
    │           Any output data that we produced
    │
    ├── environment.yml
    └── environment_frozen.yml
            The libraries and versions that we used

## Next steps for our project

* Adding different scenarios to the temperature anamoly plot.
* [...]
* [...]

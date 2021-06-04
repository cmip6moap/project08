---

# Interactive graphics of key CMIP6-based IPCC figures

Figures in IPCC reports, especially those in the Summaries for Policy Makers, are often densely packed with information from multiple sources. This makes it challenging to understand the full impact of the figure without having additional information. This project will investigate adding interactive elements to key IPCC figures from the 5th Assessment Report or other recent Special Reports. These elements could include highlighting key aspects and relating them to key conclusions, adding numerical values or even animating graphics. The possibilities are endless.

## Contributors

* Christoph Sauter, Department of Civil and Environmental Engineering, University of Strathclyde, Glasgow, UK
* Matt Amos, Lancaster Environment Centre, Lancaster University, Lancaster, UK
* Lily Gouldsbrough, Lancaster Environment Centre, Lancaster University, Lancaster, UK
* Stephen Kelly
* Ying Chen
* Viola Heinrich, School of Geographical Sciences University of Bristol, UK
* Robert Rouse
* Project Lead: Mat Collins, University of Exeter, UK

## What was done

First we identified a few key figures from previous IPCC reports (AR5 and special reports) and discussed how the figures could be improved or made interactive to help communicate their infomation to a wider audience, mainly policy makers. 
We split up into 3 broader groups and then combined our data at the end. 

### How we approached the problem and why

[...]

### Data we used and how to obtain this

* AR6 world regions
* Historical and projected CO2 emissions data (https://esgf-node.llnl.gov/search/input4mips/)
* [...]
* [...]

### What we did during the hackathon

* Processed and analyised the respective data for input to interactive figures
* Using the world region groups that will be used in the IPCC 6th Assessment Report (AR6) we created an interactive map
* Created an interactive graph of global historical and future Net carbon emissions under different Shared Socio-Econimic Pathways (SPPs)

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

* [...]
* [...]
* [...]

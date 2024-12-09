# nitric_oxide_rgc_eLife

This repository contains the data and analysis code underlying the analyses published in [Gonschorek et al. (2024)](https://elifesciences.org/reviewed-preprints/98742v1#article-and-author-information): *"Nitric oxide modulates contrast suppression in a subset of mouse retinal ganglion cells".*

# Repository structure
The repository contains two sub-directories holding the data and code, respectively, which are structured as outlined below.

## Data
The relevant data can be found in the `data` folder. Here, the calcium- and multi-electro array (MEA) recording datasets are in two separate sub-folders.
1. **Calcium:**
    - `data/calcium_dataset` contains the following files/data:
        - `/ctrl_dataset_c1` and `ctrl_dataset_c2` contains the paired control-control dataset (C1-C2)
        - `/no_dataset_c` and `no_dataset_no` contains the paired control-NO dataset (C-NO)
        - `/stry_dataset_c` and `stry_dataset_stry` contains the paired control-strychnine dataset (C-Stry)
        - `/df_rfs` contains the paired control-NO dataset (C-Stry) for the spatial receptive fields
        - `/rgc_baden` contains the original data from [Baden et al. (2016)](https://www.nature.com/articles/nature16468#)
        - `/G32_subcluster_calcium_chirp` contains the G32 sub-clusters in response to the "chirp" stimulus
2. **MEA:**
    - `data/MEA_dataset` contains the following files/data:
        - `/Baden Types` contains the traces from [Baden et al. (2016)](https://www.nature.com/articles/nature16468#) to calculate the correlation
        - `baden_data.mat`
        - `chirp.vec` is the chirp profile
        - `MEA_dataset` contains the promprised dataset
        - `widths` contains the data used to compute the FWHM from the temporal receptive fields of G32 subclusters
        - `MEA_Data/pickle` contains the preprocessed original data
        - `MEA_Data/pickle` are the data generate in each notebook. Plus the 'clustermodelj' with j=1 to 30 and 'selected_cellsj'

## Code

The code can be found in the `code` folder; it's published under the MIT license. 
As the `data` folder structure, the `code` folder has two sub-folders.
1. **Calcium:**
    - To recreate the analyses and figure panels.

2. **MEA:**
    - To recreate the analyses of the MEA data.

# Authors and acknowledgements
See acknowledgments section in Gonschorek et al. (2024).

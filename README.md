# Stardist-Cell-Segmentation-Pipeline
## Environment set up
Python version == 3.9.x  
The commands in this section must be executed on the command line (‘Anaconda Prompt’ on Windows, ‘Terminal’ on Linux/Mac OS).  
1. Create a new conda environment with Python 3.9  
`conda create -n stardist -y python=3.9`  
2. Activate the conda environment  
`conda activate stardist`  
3. Install the required packages. For example,  
`pip install click`  
Required packages are: **click**, **numpy**, **skimage**, **scipy**, **tifffile**, **zarr**  
You can use `conda list` to check weather these packages are installed
## Usage
There are 2 files. `imgpre.py` for image preprocessing and `stardist_cell_segmentation.groovy` for cell segmentation in QuPath

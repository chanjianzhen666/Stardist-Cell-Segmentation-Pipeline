# Stardist-Cell-Segmentation-Pipeline
## Environment set up
Python version == 3.9.x  
The commands in this section must be executed on the command line (‘Anaconda Prompt’ on Windows).  
1. Create a new conda environment with Python 3.9:  
`conda create -n imgpre -y python=3.9`  
2. Activate the conda environment:  
`conda activate imgpre`  
3. Install the required packages:  
`pip install -r requirements.txt`  
Required packages are: **click**, **numpy**, **skimage**, **scipy**, **tifffile**, **zarr**  
You can use `conda list` to check weather these packages are installed
## Usage
There are 2 files. `imgpre.py` for image preprocessing and `stardist_cell_segmentation.groovy` for cell segmentation in QuPath
### Image preprocessing
1. Activate the conda environment:  
`conda activate imgpre`  
2. Change directory to where `imgpre.py` is located:  
`cd [path\to\imgpre.py]`  
For example, if your `imgpre.py` is under `C:\data\img`, then use command  
`cd C:\data\img`
3. Use command:
`python imgpre.py -m [mode] [inputpath] [outputpath]`  
For [mode] part, there are 2 modes. 'f' for preprocessing a single image, and 'd' for preprocessing all .tif or .tiff images under the input directory.
For example, if you want to preprocess `C:\data\img\img1.tiff`, and save as `C:\data\img\img1_processed.tiff`then use:  
`python imgpre.py -m f C:\data\img\img1.tiff C:\data\img\img1_processed.tiff`
If you want to preprocess all images under `C:\data\img\imc`, and save them under `C:\data\img\imc_processed`, then use:  
`python imgpre.py -m d C:\data\img\imc C:\data\img\imc_processed`  
What's more, if you put `imgpre.py` in the same directory with images to be processed, then you can just use:  
`python imgpre.py -m f img1.tiff img1_processed.tiff`  
Use command `python imgpre.py --help` for more help
### Cell segmentation
1. Open QuPath, open a project
2. Drag `stardist_cell_segmentation.groovy` into the QuPath window
3. Run the scrip by *Run -> Run for project*

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
You can use `conda list` to check weather these packages are installed

## Usage
There are 2 files. `imgpre.py` for image preprocessing and `stardist_cell_segmentation.groovy` for cell segmentation in QuPath

### Image preprocessing
1. Activate the conda environment:  
`conda activate imgpre`  
2. Change directory to where `imgpre.py` is located:  
`cd [path\to\imgpre.py]`  
For example, if your `imgpre.py` is under `C:\data\img`, then use command:  
`cd C:\data\img`
3. Use command:  
`python imgpre.py [options] [inputpath] [outputpath]`  
options are:
    - -m: mode. There are 2 modes. 'd' for preprocessing all .tif or .tiff images under the input directory (default), and 'f' for preprocessing a single image.  
      For example, if you want to preprocess `C:\data\img\img1.tiff`, and save as `C:\data\img\img1_processed.tiff`, then use:  
      `python imgpre.py -m f C:\data\img\img1.tiff C:\data\img\img1_processed.tiff`  
      What's more, if you put `imgpre.py` in the same directory with images to be processed, then you can just use:  
      `python imgpre.py -m f img1.tiff img1_processed.tiff`  
      If you want to preprocess all images under `C:\data\img\imc`, and save them under `C:\data\img\imc_processed`, then use:  
      `python imgpre.py -m d C:\data\img\imc C:\data\img\imc_processed`  
      or just:  
      `python imgpre.py imc imc_processed`
    - -s: sigma, which is the argument for Gaussian filter. Default is 1.0.
    - -o: the argument for open operation. Default is 5.

    Use command `python imgpre.py --help` for more help.

### Cell segmentation
1. Open QuPath, install StarDist extension following [this](https://github.com/qupath/qupath-extension-stardist).
2. Open a project.
3. Drag `stardist_cell_segmentation.groovy` into the QuPath window.
4. Run the scrip by *Run -> Run for project*.
5. Select images to be processed.
6. The result is saved as a .geojson file under `[project directory]\json`.
7. If a segmentation mask image is needed, place `json_to_tiff.py` under the project directory and run it under the environment mentioned before, the mask image will be generated under `[project directory]\masks`.

## Downstream process

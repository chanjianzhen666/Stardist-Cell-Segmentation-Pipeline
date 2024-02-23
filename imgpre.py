import os
import click
import numpy as np
from tifffile import imread, imwrite
import zarr
from skimage.exposure import equalize_adapthist
from skimage.filters.thresholding import threshold_otsu
import scipy.ndimage as ndi

def img_preprocess(img, sigma, open_size):
    # Adjust image contrast by adaptively equalizing the histogram
    img_equalized_adapted = equalize_adapthist(img, kernel_size=None)

    img = img_equalized_adapted
    img = (((img - img.min()) / (img.max() - img.min())) * 255).astype('uint8')

    # Apply the filter and allocate the output to a new variable.
    img_smooth = ndi.gaussian_filter(img, sigma)

    # Foreground detection
    thresh = threshold_otsu(img_smooth)
    mem_adapted = img_smooth > thresh
    mem = mem_adapted
    i = open_size
    SE = (np.mgrid[:i,:i][0] - np.floor(i/2))**2 + (np.mgrid[:i,:i][1] - np.floor(i/2))**2 <= np.floor(i/2)**2
    pad_size = i + 1
    mem_padded = np.pad(mem, pad_size, mode='reflect')
    mem_final = ndi.binary_opening(mem_padded, structure=SE)
    mem_final = mem_final[pad_size:-pad_size, pad_size:-pad_size]
    img_final = img * mem_final
    return img_final

@click.command()
@click.option('--mode', '-m', default='d', help="Choose processing mode, 'd' for all files under the directory (default), 'f' for a sigle file")
@click.option('--sigma', '-s', default=1.0, help="Gaussian filter argument")
@click.option('--open_size', '-o', default=5, help="Open operation argument")
@click.argument('inputpath')
@click.argument('outputpath')
def main(mode, sigma, open_size, inputpath, outputpath):
    if mode == 'f':
        store = imread(inputpath, aszarr=True)
        z = zarr.open(store, mode='r')
        
        if z.name == None:
            img = z
            img_processed = img_preprocess(img, sigma, open_size)
            imwrite(outputpath, img_processed)
            click.echo('Done!')
        
        elif z.name == '/':
            z = z[0]
            height = z.shape[0]
            width = z.shape[1]
            img_final = zarr.zeros((height, width), dtype='uint8')
            height_per_tile = height // 2
            
            for i in range(2):
                img = z[i*height_per_tile:(i+1)*height_per_tile, :, 0]
                img = (((img - img.min()) / (img.max() - img.min())) * 255).astype('uint8')
                img_preprocessed = img_preprocess(img, sigma, open_size)
                img_final[i*height_per_tile:(i+1)*height_per_tile, :] = img_preprocessed

            imwrite(outputpath, img_final)
            click.echo('Done!')
            store.close()
    
    if mode == 'd':
        files = os.listdir(inputpath)
        if not os.path.exists(outputpath):
            os.makedirs(outputpath)
        for file in files:
            if str(file).endswith('.tif') or str(file).endswith('.tiff'):
                img = imread(inputpath + '\\' + file)
                img_processed = img_preprocess(img, sigma, open_size)
                imwrite(outputpath + '\\' + str(file), img_processed)
                click.echo(str(file) + ' done')
        click.echo('All done!')

if __name__ == '__main__':
    main()

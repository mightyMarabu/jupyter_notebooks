import argparse
import rasterio as rio
from sklearn import cluster
import matplotlib.pyplot as plt
import numpy as np

def main(root_directory, image):
    # Open the raster image
    raster = rio.open(root_directory+'/'+image)
    
    # Read raster data into numpy array
    arr = raster.read()
    
    # Reshape raster data for clustering
    imgxyb = np.empty((raster.count, raster.height, raster.width), raster.meta['dtype'])
    for band in range(imgxyb.shape[0]):
        imgxyb[band,:,:] = raster.read(band+1)
    
    img1d = imgxyb[:10,:,:].reshape((imgxyb.shape[1]*imgxyb.shape[2],imgxyb.shape[0]))
    
    # Perform KMeans clustering
    cl = cluster.KMeans(n_clusters=10)
    param = cl.fit(img1d)
    cl.labels_

    # Get the labels of the classes and reshape it x-y-bands shape order (one band only)
    img_cl = cl.labels_
    img_cl = img_cl.reshape(imgxyb[0,:,:].shape)
    img_cl.shape
    
    # Define colormap
    cmap="RdYlGn_r"
    
    # Show the resulting array
    plt.figure(figsize=[20,20])
    plt.imshow(img_cl, cmap=cmap)
    plt.axis('off')
    plt.show()

    # Define the output file path
    output_file = root_directory+'/'+"classified_"+image

    # Update the metadata for the output file
    transform = raster.transform
    height, width = img_cl.shape
    count = 1  # assuming a single band
    dtype = rio.uint8  # update with the appropriate data type

    # Write the result to the output file
    with rio.open(output_file, 'w', driver='GTiff', height=height, width=width, count=count, dtype=dtype, crs=raster.crs, transform=transform) as dst:
        dst.write(img_cl, 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="KMeans clustering on raster images")
    parser.add_argument("root_directory", type=str, help="Root directory of the raster image")
    parser.add_argument("image", type=str, help="Filename of the raster image")
    args = parser.parse_args()

    main(args.root_directory, args.image)

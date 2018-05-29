import boto3
import pandas as pd
import re
from osgeo import gdal
import numpy as np
import utm
import os
from osgeo import gdal, gdalnumeric, ogr, osr
import pdb
import pickle
from numpy import genfromtxt


def world2Pixel(geoMatrix, x, y,lat):
    """
    Uses a gdal geomatrix (gdal.GetGeoTransform()) to calculate
    the pixel location of a geospatial coordinate
    """
    if lat>=0:
        ulX = geoMatrix[0]
        ulY = geoMatrix[3]
        xDist = geoMatrix[1]
        yDist = geoMatrix[5]
        rtnX = geoMatrix[2]
        rtnY = geoMatrix[4]
        pixel = int((x - ulX) / xDist)
        line = int((ulY - y) / yDist)
        return (np.absolute(pixel), np.absolute(line))
    else:
        ulX = geoMatrix[0]
        ulY = geoMatrix[3] + 10000000
        xDist = geoMatrix[1]
        yDist = geoMatrix[5]
        rtnX = geoMatrix[2]
        rtnY = geoMatrix[4]
        pixel = int((x - ulX) / xDist)
        line = int((ulY-y) / yDist)
        return (np.absolute(pixel), np.absolute(line))


def mean_med_pixel(df,scene_dict,Xmat_mean,Xmat_median):
    """ Uses VSIS3 to pull a 7x7 pixel grid around a utm coordinate
    and adds the mean and median values to np arrays.
    Saves np matrices in csv files """

    for p_r_y in scene_dict.keys():
        path, row, year = p_r_y
        path = int(path)
        row = int(row)
        year = int(year)

        inds = df.index[(df.path==path) & (df.row==row) & (df.vintage==year)].tolist()
        for j,file_name in enumerate(scene_dict[p_r_y]):
            try:
                vspath = '/vsis3/landsat-pds/' + file_name
                ds = gdal.Open(vspath)
                geoTrans = ds.GetGeoTransform()

                for i in inds:
                    lat = df.iloc[i,-5]
                    lon = df.iloc[i,-4]

                    x,y ,_ , __= utm.from_latlon(lat, lon)
                    Xp, Yp = world2Pixel(geoTrans,x,y,lat)

                    band = ds.GetRasterBand(1)
                    np_array = band.ReadAsArray(int(Xp-3), int(Yp-3), int(7), int(7))
                    #pdb.set_trace()
                    Xmat_mean[i,j] = np.mean(np_array)
                    Xmat_median[i,j] = np.median(np_array)
            except:
                print(i,j,'not updated')
                break

    np.savetxt('Xmean2017.csv',Xmat_mean,delimiter = ',')
    np.savetxt('Xmedian2017.csv',Xmat_mean,delimiter = ',')





if __name__ == '__main__':

    with open('../data/scene_dict2017.pkl', 'rb') as f:
        scene_dict = pickle.load(f)

    df = pd.read_csv('unique_latlong.csv')

    Xmat_mean = np.zeros((df.shape[0],286))
    Xmat_median = np.zeros((df.shape[0],286))

    # Xmat_mean = genfromtxt('Xmean2017.csv', delimiter=',')
    # Xmat_median = genfromtxt('Xmedian2017.csv', delimiter=',')

    #index21 not updataed 097 084 2015



    mean_med_pixel(df,scene_dict,Xmat_mean,Xmat_median)

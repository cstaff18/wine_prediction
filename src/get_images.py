import utm
import os
from osgeo import gdal, gdalnumeric, ogr, osr
import numpy as np
import pandas as pd
import boto3
import re

def world2Pixel(geoMatrix, x, y):
    """
    Uses a gdal geomatrix (gdal.GetGeoTransform()) to calculate
    the pixel location of a geospatial coordinate
    """
    ulX = geoMatrix[0]
    ulY = geoMatrix[3]
    xDist = geoMatrix[1]
    yDist = geoMatrix[5]
    rtnX = geoMatrix[2]
    rtnY = geoMatrix[4]
    pixel = int((x - ulX) / xDist)
    line = int((ulY - y) / yDist)
    return (pixel, line)


def get_image(dirpath, lat, long):
    #opens image from local machine and returns croped image

    directory = os.fsencode(dirpath)
    is_image = False

    x,y ,_ , __= utm.from_latlon(lat, long)

    image = np.zeros((12,7,7))

    j = 0
    for i, file in enumerate(os.listdir(directory)):
        filename = os.fsdecode(file)
        if filename.endswith(".TIF") or filename.endswith(".tif"):

            # print(os.path.join(directory, filename))
            srcArray = gdalnumeric.LoadFile(dirpath + '/' + filename)

            # Also load as a gdal image to get geotransform
            # (world file) info
            srcImage = gdal.Open(dirpath + '/' + filename)
            geoTrans = srcImage.GetGeoTransform()

            #gets 10^2 acres surrounding lat long
            ulX, ulY = world2Pixel(geoTrans,x+100,y+100)
            lrX, lrY = world2Pixel(geoTrans,x-100,y-100)

            clip = srcArray[lrY:lrY +7, ulX:ulX + 7]

            image[j,:,:] = clip
            j+=1

        else:
            continue

    return image


def get_growing_season(df):
    #loop through all images in a single year

    #image_size
    i_s = 7
    #n images in season
    k = 15
    images = []
    for i in range(df.shape[0]):
        r = df.iloc[i,:]

        path = r.path
        row = r.row
        year = r.vintage
        lat = r.lat
        lon = r.long

        image = np.zeros((12,7*k,7))

        dirpath = '/Users/Coho/DSI/webscrape/LANDSAT-Download/mnt/data/LANDSAT8/N{0}_{1}_{2}'.format(path,row,year)

        l = 0
        for d in os.listdir(dirpath):
            if d.endswith("T1"):
                subdir = os.fsdecode(d)

                subdirname = dirpath + '/' + d

                image[:,l*7:l*7 +7,:] = get_image(subdirname,lat,lon)
                l += 1
                print('Band {}'.format(l))

        images.append(image)
        print('{} completed'.format(i))

    return images


def get_average_pixels(dirpath, lat, long):
    #calc average pixel intensity from cropped photo

    directory = os.fsencode(dirpath)
    is_image = False

    x,y ,_ , __= utm.from_latlon(lat, long)

    image = np.zeros((1,12))

    j = 0
    for i, file in enumerate(os.listdir(directory)):
        filename = os.fsdecode(file)
        if filename.endswith(".TIF") or filename.endswith(".tif"):

            # print(os.path.join(directory, filename))
            srcArray = gdalnumeric.LoadFile(dirpath + '/' + filename)

            # Also load as a gdal image to get geotransform
            # (world file) info
            srcImage = gdal.Open(dirpath + '/' + filename)
            geoTrans = srcImage.GetGeoTransform()

            #gets 10^2 acres surrounding lat long
            ulX, ulY = world2Pixel(geoTrans,x+100,y+100)
            lrX, lrY = world2Pixel(geoTrans,x-100,y-100)

            clip = srcArray[lrY:lrY +7, ulX:ulX + 7]

            image[0,j] = np.mean(clip)
            j+=1

        else:
            continue

    return image

def get_growing_season_average_pixel(df):
    #get average pixels from AWS images

    #n images in season
    k = 15
    images = np.zeros((df.shape[0],12*k))
    for i in range(df.shape[0]):
        r = df.iloc[i,:]

        path = r.path
        row = r.row
        year = r.vintage
        lat = r.lat
        lon = r.long

        image = np.zeros((1,12*15))
        dirpath = '/Users/Coho/DSI/webscrape/LANDSAT-Download/mnt/data/LANDSAT8/N{0}_{1}_{2}'.format(path,row,year)

        l = 0
        for d in os.listdir(dirpath):
            if d.endswith("T1"):
                subdir = os.fsdecode(d)

                subdirname = dirpath + '/' + d

                image[0,(l*12):(l*12)+12] = get_average_pixels(subdirname,lat,lon)
                l += 1
                print('Band {}'.format(l))
        #print(image)
        images[i,:] = image
        print('{} completed'.format(i))

    return images


def get_average_pixels_aws(dirpath, lat, long):

    client = boto3.client('s3') #low-level functional API
    resource = boto3.resource('s3') #high-level object-oriented API
    my_bucket = resource.Bucket('landsat-pds')
    files = list(my_bucket.objects.filter(Prefix=dirpath))
    is_image = False

    x,y ,_ , __= utm.from_latlon(lat, long)

    image = np.zeros((1,12))

    j = 0
    for i, f in enumerate(files):
        filename = f.key
        if filename.endswith(".TIF") or filename.endswith(".tif"):

            # print(os.path.join(directory, filename))
            srcArray = gdalnumeric.LoadFile(filename)

            # Also load as a gdal image to get geotransform
            # (world file) info
            srcImage = gdal.Open(filename)
            geoTrans = srcImage.GetGeoTransform()

            #gets 10^2 acres surrounding lat long
            ulX, ulY = world2Pixel(geoTrans,x+100,y+100)
            lrX, lrY = world2Pixel(geoTrans,x-100,y-100)

            clip = srcArray[lrY:lrY +7, ulX:ulX + 7]

            image[0,j] = np.mean(clip)
            j+=1

        else:
            continue

    return image

def get_images_from_bucket(df):
    #set up image location dump
    k = 15
    images = np.zeros((df.shape[0],12*k))

    #set up amazon bucket path
    client = boto3.client('s3') #low-level functional API
    resource = boto3.resource('s3') #high-level object-oriented API
    my_bucket = resource.Bucket('landsat-pds') #subsitute this for your s3 bucket name.


    for i in range(df.shape[0]):
        r = df.iloc[i,:]

        path = str(r.path)
        row = str(r.row)
        year = r.vintage
        lat = r.lat
        lon = r.long

        all_files = list(my_bucket.objects.filter(Prefix='c1/L8/{0}/{1}/'.format(path,row)))
        year = '2017'
        scenes = []
        for i in all_files:
            file_path = i.key
            if '_{1}{2}_{0}'.format(year,path,row) in file_path:
                scenes.append(file_path)

        folder_list = []
        for s in scenes:
            folder_name = re.search('c1/L8/{0}/{1}/(.+?)/'.format(path,row), s)
            if folder_name.groups(1)[0].endswith('T1'):
                folder_list.append(folder_name.groups(1)[0])
        folder_list = set(folder_list)

        l = 0
        for folder in folder_list:
            path = 'c1/L8/{0}/{1}/{2}'.format(path,row,folder)
            image[0,(l*12):(l*12)+12] = get_average_pixels_aws(path,lat,lon)





if __name__ == '__main__':

    df = pd.read_csv('pinot_noir_date_pathrow.csv')

    df1 = df[df.path == 43][df.row == 35]
    X = get_growing_season_average_pixel(df1)
    df2 = df[df.path == 43][df.row == 36]
    X = np.append(X,get_growing_season_average_pixel(df2),axis = 0)
    df3 = df[df.path == 45][df.row == 33]
    X = np.append(X,get_growing_season_average_pixel(df3),axis = 0)
    df4 = df[df.path == 46][df.row == 29]
    X = np.append(X,get_growing_season_average_pixel(df4),axis = 0)

    y = df1.points.values
    y = np.append(y,df2.points.values)
    y = np.append(y,df3.points.values)
    y = np.append(y,df4.points.values)



    # X1 = get_growing_season(df1)
    # y1 = df1.points.values
    #
    # df2 = df[df.path == 43][df.row == 36]
    # X2 = get_growing_season(df2)
    # y2 = df2.points.values
    #
    # df3 = df[df.path == 45][df.row == 33]
    # X3 = get_growing_season(df3)
    # y3 = df1.points.values
    #
    # df4 = df[df.path == 46][df.row == 29]
    # X4 = get_growing_season(df1)
    # y4 = df1.points.values

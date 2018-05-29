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

'''
explores the landsat s3 bucket and retrieves the paths to files for each
path, row, year for the 2016-17 naming convention
'''

def create_dict (df):
    scene_dict = {}
    for i in range(df.shape[0]):
        j = 0
        r = df.iloc[i,:]

        path = str(int(r.path))
        while len(path) < 3:
            path = '0' + path
        row = str(int(r.row))
        while len(row) < 3:
            row = '0' + row
        year = str(int(r.vintage))

        if (path,row,year) in scene_dict:
            pass
        else:
            scene_dict[(path,row,year)] =[]
    return scene_dict

def fill_dict(df,scene_dict):
    client = boto3.client('s3')
    resource = boto3.resource('s3')
    my_bucket = resource.Bucket('landsat-pds')

    for p_r_y in scene_dict.keys():
        path, row, year = p_r_y
        get_scenes = []
        all_files = list(my_bucket.objects.filter(Prefix='c1/L8/{0}/{1}/'.format(path,row)))
        scenes = []
        for ind in all_files:
            file_path = ind.key
            if '{1}{2}_{0}'.format(year,path,row) in file_path:
                scenes.append(file_path)

        folder_list = []
        for s in scenes:
            folder_name = re.search('c1/L8/{0}/{1}/(.+?)/'.format(path,row), s)
            folder_list.append(folder_name.groups(1)[0])
        folder_list = set(folder_list)

        for folder in folder_list:
            files = list(my_bucket.objects.filter(Prefix='c1/L8/{0}/{1}/{2}'.format(path,row,folder)))

            for f in files:
                file_name = f.key
                if file_name.endswith('TIF'):
                    get_scenes.append(file_name)
        scene_dict[p_r_y] = get_scenes

    return scene_dict


if __name__ == '__main__':
    df = pd.read_csv('unique_latlong.csv')
    scene_dict = create_dict(df)
    scene_dict = fill_dict(df,scene_dict)

    with open('../data/scene_dict2017.pkl', 'wb') as f:
        pickle.dump(scene_dict, f, pickle.HIGHEST_PROTOCOL)

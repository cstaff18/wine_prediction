import ogr
import shapely.wkt
import shapely.geometry
import urllib
import zipfile
import pandas as pd




def checkPoint(feature, point, mode):
    geom = feature.GetGeometryRef() #Get geometry from feature
    shape = shapely.wkt.loads(geom.ExportToWkt()) #Import geometry into shapely to easily work with our point
    if point.within(shape) and feature['MODE']==mode:
        return True
    else:
        return False


def get_path_row(lat,lon):
    shapefile = 'wrs2_asc_desc/wrs2_asc_desc.shp'
    wrs = ogr.Open(shapefile)
    layer = wrs.GetLayer(0)

    i=0
    point = shapely.geometry.Point(lon, lat)
    mode = 'D'
    while not checkPoint(layer.GetFeature(i), point, mode):
        i += 1
    feature = layer.GetFeature(i)
    path = feature['PATH']
    row = feature['ROW']
    return path, row


def update_df(df):
    df['path'] = 0
    df['row'] = 0
    i = 0
    for la, lo in zip(df['lat'],df['long']):
        print(la,lo)
        path, row = get_path_row(la,lo)
        df.iloc[i,-2] = path
        df.iloc[i,-1] = row
        i += 1
        if i%100 == 0: print('{} records updates'.format(i))

    return df

if __name__ == '__main__':
    df = pd.read_csv('pinot_noir_with_lat_lon.csv')
    df = df[df.vintage == 2014]
    df = df[df.lat > 0]
    df = update_df(df)

    df.to_csv('pinot_noir_with_path_row.csv')

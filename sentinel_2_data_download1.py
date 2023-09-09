# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 17:38:53 2023

@author: MSKT09
"""

#data download

from sentinelsat import SentinelAPI
import geopandas as gpd
from datetime import datetime

# Set up your Sentinel Hub account credentials
API_USERNAME = 'micronetproduction23'  # Replace with your own username
API_PASSWORD = 'Micronet@2023'  # Replace with your own password

# Set up the SentinelAPI
api = SentinelAPI(API_USERNAME, API_PASSWORD, 'https://scihub.copernicus.eu/dhus')

# Define the Area of Interest (AOI) using a shapefile
aoi_shapefile_path = r'D:\python\Sentinel_2_downlode\Achalpur_shapefile\achalpur.shp'   # Replace with the path to your AOI shapefile

# Read the shapefile using geopandas
aoi = gpd.read_file(aoi_shapefile_path, encoding='utf-8')

# Extract the geometry of the AOI
footprint = aoi.geometry.values[0]

# Define the date range
start_date = datetime.strptime('2019-09-01', '%Y-%m-%d').strftime('%Y%m%d')
end_date = datetime.strptime('2019-09-15', '%Y-%m-%d').strftime('%Y%m%d')



# Search for Sentinel-2 images within the defined AOI and date range
products = api.query(footprint,
                     date=(start_date, end_date),
                     platformname='Sentinel-2',
                     producttype='S2MSI1C')


# Download the images as zip files
api.download_all(products, directory_path=r'D:\python\Sentinel_2_downlode\Downloded_images\sep_2019')

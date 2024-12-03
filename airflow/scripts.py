import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import io
from request_data import get_data
from mongoconnection import MongoDBConnector
import os

def get_meta_data(query_meta : str):
    meta_data = get_data(query_meta).json()
    return meta_data

def safe_images(query_img : str,query_meta : str):
    meta_data = get_data(query_meta).json()

    folder_path = "airflow/airflow/extracted_images/"
    file_name = "name"#meta_data["date"][0:9]

    full_path = folder_path+file_name+".png"

    image_stream = io.BytesIO(get_data(query_img).content)
    img = mpimg.imread(image_stream, format='png')
    plt.imshow(img)
    plt.savefig(full_path)
    return img

def store_in_db(data):
    MongoDBCon = MongoDBConnector(
        hostname="localhost", 
        port=2717, 
        username="rootuser", 
        password="rootpass"
        )
    connector = MongoDBCon.connect()

    print(connector.list_database_names())

    NasaDb = connector["NasaData"]
    NasaTable = NasaDb["SatelliteData"]
    NasaTable.insert_one(data)
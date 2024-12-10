from scripts import safe_images,store_in_db,get_meta_data

IMAGE_QUERY_URL: str = "https://api.nasa.gov/planetary/earth/imagery"

IMAGE_DATA_QUERY_URL : str = "https://api.nasa.gov/planetary/earth/assets"

#image = safe_images(IMAGE_QUERY_URL,IMAGE_DATA_QUERY_URL)

store_in_db(get_meta_data(IMAGE_DATA_QUERY_URL))
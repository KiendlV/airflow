import pymongo

class MongoDBConnector:
    def __init__(self, hostname="localhost", port=27017, username=None, password=None):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.connector = None
    
    def connect(self):
        try:
            connection_string = f"mongodb://{self.hostname}:{self.port}/"
            self.connector = pymongo.MongoClient(
                connection_string,
                username=self.username,
                password=self.password
            )
            print("Connected to MongoDB successfully!")
            return self.connector
        except Exception as e:
            print("Error connecting to MongoDB:", e)
            return None

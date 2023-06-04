from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):

        # USER = 'aacuser'
        # PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31472  # Personalize PORT number
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % DB]
        self.collection = self.database['%s' % COL]
        
        # Will print if connection occurs
        print("Connection Successful")

# Complete this method to implement the "create" in CRUD.
    def create(self, data):
        
        try:
            if data is not None:
                # Passes argument from Jupyter to the database to insert index
                self.database.animals.insert_one(data)
                return True
            
            else:
                raise Exception("Nothing to save, because data parameter is empty")
                return False
            
          #  Exception handling
        except Exception as e:
            print("An exception occurred ::", e)

# Create method to implement the "read" in CRUD.
    def read(self, data):
        try:
            if data is not None:
                # Passes search argument and returns back the query
                query = list(self.database.animals.find(data))
                return query
            
         # Exception Handling
        except Exception as e:
            print("An exception occurred ::", e)
        
        



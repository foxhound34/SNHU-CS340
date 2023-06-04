from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):

        #USER = 'aacuser'
        #PASS = 'SNHU1234'  # I kept the same password from the prompt
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31472  # Personalize PORT number
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
        #Will print if connection occurs
        print("Connection Successful")

# Complete this method to implement the "create" in CRUD.
    def create(self, data):
        
        try:
            if data is not None:
                #Passes argument from Jupyter to the database to insert index
                self.database.animals.insert_one(data)
                return True
            
            else:
                raise Exception("Nothing to save, because data parameter is empty")
                return False
            
          #Exception handling  
        except Exception as e:
            print("An exception occurred ::", e)

# Create method to implement the "read" in CRUD.
    def read(self, readdata):
        try:
            if readdata is not None:
                #Passes search argument and returns back the query
                query = list(self.database.animals.find(readdata))
                return query
            else:
                return {}
            
         #Exception Handling   
        except Exception as e:
            print("An exception occurred ::", e)
        
# Create method to implement the "update" in CRUD.
    def update(self, readData, updateData):
        try:
            if readData is not None:
                #Passes search argument and returns back the query
                index_update = self.database.animals.update(readData, {"$set":updateData})
                return index_update
            
            else:
                return {}
             
          #Exception Handling   
        except Exception as e:
            print("An exception occurred ::", e)       


# Create method to implement the "delete" in CRUD.
    def delete(self, data):
        try:
            if data is not None:
                #Passes search argument and returns back the query
                delete= self.database.animals.delete_many(data)
                return delete
                          
            else:
                return {}
            
         #Exception Handling   
        except Exception as e:
            print("An exception occurred ::", e)
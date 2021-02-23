from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

class CRUD(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, port, db, collection, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        uri = "mongodb://"+ username+":"+password+"@localhost:"+port+"/admin"
        client = MongoClient(uri)
        self.client = client
        self.database = self.client[db]
        self.collection = self.database[collection]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            if isinstance(data, dict):
                self.collection.insert_one(data)  # data should be dictionary
                return True
                
            else:
                raise Exception("data type error: data parameter is not a dictionary")
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        return False

# Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            if isinstance(query, dict):
                i = 0
                docHolder = []
                for document in self.collection.find(query):
                    i = 1  
                    docHolder.append(document)
                if i != 0:
                    return self.collection.find(query,{"_id":False})
                    
                else:
                    print("query not found in collection")
            else:
                print("data type error: data parameter is not a dictionary")
                raise Exception("data type error: data parameter is not a dictionary")
        else:
            print("Nothing to find, because given query is empty")
            raise Exception("Nothing to find, because given query is empty")
    
#Update method to implement U in CRUD
    def update(self, query, data):
        if data is not None:
            if isinstance(data, dict):
                if query is not None:
                    if isinstance(query, dict):
                        results = self.collection.update_many(query, {'$set':data})
                        
                        return results.raw_result
                    else:
                        print("data type error: query parameter is not a dictionary")
                        raise Exception("data type error: query parameter is not a dictionary")
                else:
                    print("error: given query is empty")
                    raise Exception("given query is empty")
            else:
                print("data type error: data parameter is not a dictionary")
                raise Exception("data type error: data parameter is not a dictionary")
        else:
            print("error: given data is empty")
            raise Exception("given data is empty")
            
    #delete method to implement D in CRUD
    def delete(self, query):
        if query is not None:
            if isinstance(query, dict):
                results = self.collection.delete_one(query)      
                return results.raw_result
            else:
                print("data type error: data parameter is not a dictionary")
                raise Exception("data type error: data parameter is not a dictionary")
        else:
            print("Nothing to find, because given query is empty")
            raise Exception("Nothing to find, because given query is empty")
        
            
                        

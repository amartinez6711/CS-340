# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        username = 'aacuser'
        password = 'CS340'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31350
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:            
            result = self.database.animals.insert(data) # data should be dictionary     
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

 # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            cursor = self.database.animals.find(data)
        else: 
            raise Exception("No records found")
        return cursor 
 # Create method to implement the U in CRUD
    def update(self,data, update_data):
        if data is not None:
            result = self.database.animals.update_many(data, {'$set':update_data})   
            return True
        else:
            raise Exception("Nothing to update, because data parameter is empty")
 # Create method to implement the D in Crud
    def delete(self,data):
        if data is not None:
            self.database.animals.delete_many(data)
            return True
        else:
            raise Exception("Couldn't find record to delete")
            
        

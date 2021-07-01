#!/usr/bin/python3
import time
import glob
from tinydb import TinyDB, Query



class FileDao():

    def __init__(self): # constructor
        super().__init__()
        self.getCollectionIDs()
        
    # creat methods
    def createCollection(self, cardGame): 
        identifier = str(int(time.time()*10000000)) # guarantees a unique name
        json = TinyDB('data/collections/' +identifier +'.json')

        json.insert({'field' : 'identifer', 'value' : identifier})
        json.insert({'field' : 'game', 'value' : cardGame})
        json.insert({'field' : 'name', 'value' : cardGame +' Collection'})
        json.insert({'field' : 'colorScheme', 'value' : 'scheme0'})
        json.insert({'field' : 'containers', 'value': []})
        
        query = Query() 
        print(json.all())
        #json.update({'value': 'Kagamine'}, query['field'] == 'name')
        #print(json.search(query['field'] == 'name')[0].get('value'))
        thing = json.search(query['field'] == 'containers')[0].get('value')
        print(thing)
        thing.append({'container' : '123456'})
        print(thing)
        json.update({'value': thing}, query['field'] == 'containers')
        print(json.all())

        # adding a new container
        containers = json.search(query['field'] == 'containers')[0].get('value')
        containers.append({'container' : '123456'})
        json.update({'value': containers}, query['field'] == 'containers')

        print(json.all())
        return True
    #
    def createContainer(self, collectionID):
        identifier = str(int(time.time()*10000000)) # guarantees a unique name
        json = TinyDB('data/containers/' +identifier +'.json')

        json.insert({'field' : 'identifer', 'value' : identifier})
        json.insert({'field' : 'collectionID', 'value' : collectionID})
        json.insert({'field' : 'name', 'value' : 'Container'})
        json.insert({'field' : 'colorScheme', 'value' : 'scheme0'})
        json.insert({'field' : 'cards', 'value': []})
        return True

    # read methods
    def getCollectionIDs(self):
        IDs = []
        for file in glob.glob("data/collections/*.json"):
            id = file[17 : 34] # this trims the things around the * off the id
            IDs.append(id)
        return IDs
    
    def getCollectionData(self, collectionID, field):
        json = TinyDB('data/collections/' +collectionID +'.json')
        query = Query() 

        data = json.search(query['field'] == field)[0].get('value')
        if isinstance(data, list):
            return self.getListValues(data, field)
        return data
        #
    def getContainerData(self, containerID, field):
        json = TinyDB('data/containers/' +containerID +'.json')
        query = Query() 

        data = json.search(query['field'] == field)[0].get('value')
        if isinstance(data, list):
            return self.getListValues(data, field)
        return data

    # update methods
    def updateCollectionData(self, collectionID, field, data):
        print('Update Collection Data')
        return True
        #
    def updateContainerData(self, containerID, field, data):
        print('Update Container Data')
        return True

    # delete methods
    def deleteCollection(self, collectionID):
        print('Delete Collection')
        return True
    #
    def deleteContainer(self, containerID):
        print('Delete Container')
        return True
    
    # utility methods
    def getListValues(self, data, field):
        dataList = []
        for dat in data:
            dataList.append(dat.get(field))
        return dataList














    def populate(self):
        print('Populate')


def main():
    run = FileDao()
    

if __name__ == '__main__':
    main()
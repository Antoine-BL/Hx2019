import json
import math

class pathData : 

    def __init__(self, fileName):
        self.mapData = {}
        with open(fileName) as file :
            data = json.load(file)
            for feature in data['features']:
                for line in feature['geometry']['coordinates']:
                    self.mapData[(line[0][0], line[0][1])] = {'id': feature['properties']['ID'], 'reverse': False}
                    self.mapData[(line[-1][0], line[-1][1])] = {'id': feature['properties']['ID'], 'reverse': True}


    def findClosestPath(self, coord):

        distance = 10000000000000000000
        featureId = 0

        for key, value in self.mapData.items() :
            dist = (coord[0] - key[0])**2 + (coord[1] - key[1])**2 
            if (dist < distance) :
                featureId = value['id']
                distance = dist
        return featureId

    def makePath(self, coord1, coord2):
        
        
    
map = pathData('montreal.json')
print (map.findClosestPath((-73.96219789981842, 45.41612831487927)))
print (map.findClosestPath((-73.9369797706604, 45.44953407110633)))


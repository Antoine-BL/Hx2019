import json
import math
from collections import defaultdict

class pathData : 

    def __init__(self, fileName):
        self.mapData = defaultdict(list)
        with open(fileName) as file :
            data = json.load(file)
            for feature in data['features']:
                for line in feature['geometry']['coordinates']:
                    self.mapData[(line[0][0], line[0][1])].append({'id': feature['properties']['ID'], 'endPoint': (line[-1][0], line[-1][1]), 'path': line})
                    self.mapData[(line[-1][0], line[-1][1])].append({'id': feature['properties']['ID'], 'endPoint': (line[0][0], line[0][1]), 'path': line})


    def findClosestPath(self, coord):

        distance = 10000000000000000000
        segments = None

        for key, value in self.mapData.items() :
            dist = (coord[0] - key[0])**2 + (coord[1] - key[1])**2 
            if (dist < distance) :
                segments = value
                distance = dist
        return segments

    def findCLosestPathCoordinate(self, coord):
        distance = 10000000000000000000
        coordinate = None

        for key, value in self.mapData.items() :
            dist = (coord[0] - key[0])**2 + (coord[1] - key[1])**2 
            if (dist < distance) :
                coordinate = key
                distance = dist
        return coordinate

    def makePath(self, coord1, coord2):
        path = []
        segment = self.findClosestPath(coord1)[0]
        nextPath = segment['endPoint']
        while (nextPath != self.findCLosestPathCoordinate(coord2) or nextPath == None):
            path.append(segment['id'])
            if len(self.mapData[nextPath]) < 2:
                break
            for p in self.mapData[nextPath]:
                if p['id'] not in path:
                    segment = p
                    break
            nextPath = segment['endPoint']
        return path
        

        
    
map = pathData('montreal.json')
point1 = (-73.96219789981842, 45.41612831487927)
point2 = (-73.9369797706604, 45.44953407110633)
print (map.findClosestPath(point1))
print (map.findClosestPath(point2))
print (map.makePath(point1, point2))
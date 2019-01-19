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
                    self.mapData[self.roundedCoord(line[0][0:2])].append({'id': feature['properties']['ID'], 'endPoint': self.roundedCoord(line[-1][0:2]), 'path': line})
                    self.mapData[self.roundedCoord(line[-1][0:2])].append({'id': feature['properties']['ID'], 'endPoint': self.roundedCoord(line[0][0:2]), 'path': line})

    def roundedCoord(self, coord):
        return (round(coord[0], 5), round(coord[1], 5))

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
        finalPoint = self.findCLosestPathCoordinate(coord2)
        for direction in self.findClosestPath(coord1):

            segment = direction
            nextPath = segment['endPoint']
            while (nextPath != finalPoint or nextPath == None):
                path.append(segment['id'])
                if len(self.mapData[nextPath]) < 2:
                    break
                for p in self.mapData[nextPath]:
                    if p['id'] not in path:
                        segment = p
                        break
                nextPath = segment['endPoint']
            if nextPath == finalPoint :
                break
            else :
                print(path)
                path.clear()
        return path
        

        
    
map = pathData('montreal.json')
point1 = map.roundedCoord([-73.96219789981842, 45.41612831487927])
point2 = map.roundedCoord([-73.9369797706604, 45.44953407110633])
point3 = map.roundedCoord([-73.83718013763428, 45.42866626130953])
print (map.makePath(point1, point3))
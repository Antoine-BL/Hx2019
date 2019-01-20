import requests
import polyline
import json

#https://maps.googleapis.com/maps/api/directions/json?origin=45.44289515059061,-73.76473903656006&destination=45.43191889517022,-73.6774706840515&mode=bicycling&key=AIzaSyCBhoFmnGT3UQVAvedNxPGaOfpdmJBmDLM&fbclid=IwAR1B8UIEizZTmD1TlrMbEeI0gd6j47RBdNNDm1zlKv4InPlOCuCKvkArwAk%27

class googleApi :
    def __init__(self, start, end):
        self.resp = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=' + start + '&destination=' + end + '&mode=bicycling&key=AIzaSyCBhoFmnGT3UQVAvedNxPGaOfpdmJBmDLM&fbclid=IwAR1B8UIEizZTmD1TlrMbEeI0gd6j47RBdNNDm1zlKv4InPlOCuCKvkArwAk')
        self.json = self.resp.json()
    
    def getDistance(self):
        return self.json['routes'][0]['legs'][0]['distance']['value']
    
    def getData(self):
        return json.dumps({
            'distance': self.getDistance(),
            'path': polyline.decode(self.json['routes'][0]['legs'][0]['steps'][1]['polyline']['points'])
        })
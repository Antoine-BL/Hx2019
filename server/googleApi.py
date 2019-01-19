import requests
import polyline

#https://maps.googleapis.com/maps/api/directions/json?origin=45.44289515059061,-73.76473903656006&destination=45.43191889517022,-73.6774706840515&mode=bicycling&key=AIzaSyCBhoFmnGT3UQVAvedNxPGaOfpdmJBmDLM&fbclid=IwAR1B8UIEizZTmD1TlrMbEeI0gd6j47RBdNNDm1zlKv4InPlOCuCKvkArwAk%27

class googleApi :
    def __init__(self, start, end):
        self.resp = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=' + start + '&destination=' + end + '&mode=bicycling&key=AIzaSyCBhoFmnGT3UQVAvedNxPGaOfpdmJBmDLM&fbclid=IwAR1B8UIEizZTmD1TlrMbEeI0gd6j47RBdNNDm1zlKv4InPlOCuCKvkArwAk')

google = googleApi('45.44289515059061,-73.76473903656006', '45.43191889517022,-73.6774706840515')
print (google.resp.json())

print (polyline.decode(google.resp.json()['routes'][0]['legs'][0]['steps'][1]['polyline']['points']))
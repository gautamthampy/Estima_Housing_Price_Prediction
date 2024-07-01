import json
import pickle
import numpy as np
import sklearn

__model = None
__dataColumns = None
__locations = None

def loadArtifacts():
    global __dataColumns
    global __model

    with open("./artifacts/columns.json", 'r') as column:
        __dataColumns = json.load(column)['data_columns']

    with open("./artifacts/bapp.pkl", 'rb') as mlModel:
        __model = pickle.load(mlModel)

    print(__dataColumns)

def getLocation():
    loadArtifacts()
    global __locations
    __locations = __dataColumns[5:]
    return __locations

def getPredictedPrice(area, bath, bhk, location):
    loadArtifacts()
    try:
        index = __dataColumns.index(location.lower())
    except:
        index = -1

    x = np.zeros(len(__dataColumns))
    x[0] = area
    x[1] = bath
    x[2] = bhk
    if index >= 0:
        x[index] = 1

    return round(__model.predict([x])[0],2)                  


if __name__=="__main__":
    loadArtifacts()
    print(getPredictedPrice(1500,2,3,'1st phase JP Nagar'))            
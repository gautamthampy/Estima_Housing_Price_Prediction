from flask import Flask, request, jsonify
import utilities

app = Flask(__name__)

@app.route('/', methods=['GET'])
def greetings():
    return 'Welcome to Estima Server'

@app.route('/getLocation', methods=['GET'])
def getLocation():
    response = jsonify({'location':utilities.getLocation()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getPredictedPrice', methods=['GET'])
def getPredictedPrice():
    area = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])
    location = request.form['location']
    response = jsonify({
        'estimated_price':utilities.getPredictedPrice(area, bath, bhk, location)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__=="__main__":
    print("starting Estima server.....")
    utilities.loadArtifacts()
    app.run()             
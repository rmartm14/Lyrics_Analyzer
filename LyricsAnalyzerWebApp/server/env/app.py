from flask import Flask, jsonify,request
from flask_cors import CORS
import joblib

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

categories = ["The Beatles", "The Rolling Stones", "Queen", "Radiohead", "Bob Dylan"]
# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/hello', methods=['GET'])
def first():
    return jsonify("The Beatles")

@app.route('/pruebapost', methods=['POST'])
def pruebapost():
    print(request.json["song"])
    print(request.json["election"])
    return jsonify("sum")

@app.route('/clasify',methods=['POST'] )
def clasify():
    model_name = get_model_name(request.json["election"])
    model = joblib.load(model_name)
    prediction = model.predict(list(request.json["song"]))
    print(prediction)
    return jsonify(categories[prediction[0]])

#Auxiliar Methods
def get_model_name(election):
    append_route = "./pretrained_models/"
    classifiers = ["KNN.joblib", "SVM.joblib","SGDC.joblib","NB.joblib"]
    selected_classifier = classifiers[int(election)]
    return (append_route + selected_classifier)
    

if __name__ == '__main__':
    app.run()

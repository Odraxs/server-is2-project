import json

from flask import Flask, request, jsonify

from Prediccion.prueba import predecir

app = Flask(__name__)


@app.route('/')
def hello_world():
    return {'user': 'David'}

@app.route('/predict', methods=['POST'])
def predict():
    if (request.method == 'POST'):
        data=request.get_json()
        id_client=data.get("id_client")
        imagenes=data.get("images")
        modelos=data.get("models")
        predicciones=[]
        queryModelo={}
        predicciones=predecir(modelos,imagenes)
        data = {
            "message":"Predictions made satisfactorily",
            "results":predicciones
        }
        response=app.response_class(response=json.dumps(data),
                                    status=200,
                                    mimetype='application/json')
        return response


# We only need this for local development.
if __name__ == '__main__':
    app.run()

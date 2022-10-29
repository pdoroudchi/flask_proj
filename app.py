import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# create flask app
app = Flask(__name__)

# load pickle model
model = pickle.load(open('model.pkl', 'rb'))

# route to app home page, designed in "index.html" template
@app.route('/')
def home():
    return render_template('index.html')

# render results on HTML GUI
@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Predicted salary is ${}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)

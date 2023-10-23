# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gXguZM48Gp9B1NMY_jCj9PdUYGI_M3eL
"""
pip install Flask
from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
import joblib
from sklearn.preprocessing import StandardScaler


model = joblib.load('Group13_SportsPrediction.joblib')

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/')
def home():
    return render_template('index.html')


'''
@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [x_player22_test_scaled for x_player22_test_scaled in request.form.values()]
        features = np.array(features).reshape(1, -1)
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)
        prediction = model.predict(scaled_features)
        confidence = model.predict_proba(scaled_features).max()
        return render_template('index.html', prediction_text=f'Predicted Overall Rating: {prediction[0]}. Confidence: {confidence}')
    except Exception as e:
        return render_template('index.html', prediction_text='An error occurred. Please check your input data and try again.')

if __name__ == "__main__":
    app.run(debug=True)
'''


@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = []
        features = [x for x in request.form.values()]
        for feature in features:
            data.append(float(request.form[feature]))

        scaler = StandardScaler()
        input_data_scaled = scaler.transform(data)

        prediction = model.predict(input_data_scaled)[0]

        return render_template('result.html', prediction=prediction)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

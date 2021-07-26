# Importing Flask Libraries
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

# Importing libraries required for model prediction
import joblib
import json

# Other utlilities
from utils import  data_pre_process

# Initializing the app
app = Flask(__name__)


# Adding Boostrap to application
Bootstrap(app)


# Loading the saved model
saved_model = joblib.load('gbc_model.pkl')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    errors = False
    churn = None
    try:
        client_input = request.json
        clean_input = data_pre_process(client_input)
        churn = saved_model.predict(clean_input.reshape(-1,1))
    except:
        errors = True
    return {'error':errors, 'churn': churn}

if __name__ == '__main__':
    app.run()
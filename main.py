# Importing Flask Libraries
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

# Other utilities
from utils import  data_pre_process, prediction

# Initializing the app
app = Flask(__name__)


# Adding Boostrap to application
Bootstrap(app)

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
        churn = prediction(clean_input)
    except:
        errors = True
    return {'error':errors, 'churn': churn}

if __name__ == '__main__':
    app.run()
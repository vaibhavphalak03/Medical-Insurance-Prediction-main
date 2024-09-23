from flask import Flask , jsonify, request , render_template
from project_app.utlis import MedicalInsurance

app = Flask(__name__)

###########################################################################################################################
#########################################     Home   Page   API          ##################################################
###########################################################################################################################

@app.route('/')

def homepage():
    print('Medical Insurance Project')
    return 'Welcome to Medical Insurance'


@app('/preficted_charges')
def predict_charge():
    

app.run()
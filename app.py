from flask import Flask, request, jsonify
from flask import render_template,redirect,url_for
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.model_selection import train_test_split
#from sklearn.svm import SVC
#from sklearn.metrics import accuracy_score, classification_report
#from sklearn.preprocessing import StandardScaler

app = Flask(__name__,template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods = ["GET","POST"])
def predict():
    
    if request.method == "POST":

        location = request.form['city']
        day = request.form['dateInput']
        month = day[-2:].upper()
        df = pd.read_csv('database.csv')
        

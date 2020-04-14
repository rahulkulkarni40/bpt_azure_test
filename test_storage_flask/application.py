# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:30:54 2020

@author: Rahul
"""
from flask import Flask, redirect, url_for,render_template, request, jsonify,flash 
import flask
from json import dumps
import pandas as pd
from flask_cors import CORS
from azure_connection import connection 
import requests

app = flask.Flask(__name__)

app.config["DEBUG"] = False
CORS(app)

@app.route("/")
def index():
   return render_template("test.html")

@app.route('/azpost/', methods=['POST'])
def post_data():
    try:
        result = json.dumps(request.form)
        result2 = json.loads(result)
        data_send = connection(result2,"","insert")
        if data_send == "added Successfully!!!!":
            #flash('added Successfully!!!!')
            print(data_send)
            render_template("test.html")
            return str(data_send)
        else:
            return str(data_send)
        
    except requests.HTTPError as e:
        return str(e.response.content)
    
@app.route('/azget/', methods=['post'])
def get_data():
    try:
        keys = request.form["keyname"]
        keys_value = request.form["keyval"]
        print(keys,keys_value)
        query = keys + " eq " + "'" + keys_value + "'"
        print(query)
        data_send = connection("",query,"reterive")
        #data_send = connection("",query,"reterive")
        return data_send
        
    except requests.HTTPError as e:
        return str(e.response.content)

app.run()
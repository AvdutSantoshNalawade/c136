from flask import Flask,jsonify,request
from data import data
app=Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data":data,
        "massage":"success"
    }),200
@app.route("/planet")
def planet():
    name=request.args.get("name")
    planet_data=next(itom for itom in data if itom["name"]==name)
    return jsonify({
        "data":planet_data,
        "massage":"success"
    }),200
app.run()
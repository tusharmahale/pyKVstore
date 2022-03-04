# import threading, time, os
from flask import Flask, request, jsonify
import urllib.request, urllib.error
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter 

app = Flask(__name__)
metrics = PrometheusMetrics(app)
view_metric = Counter('total_no_of_keys','total_keys')

kv_store={}

@app.route("/getall")
def stats():
  try:
    return jsonify(kv_store)
  except:
    return "getAll function Error"

@app.route("/search")
def search():
  try:
    sorted_data={}
    if request.args.get('prefix'):
      prefix_data=request.args.get('prefix')
      for k in kv_store:
        if k.startswith(prefix_data):
          sorted_data[k]=kv_store[k]
    elif request.args.get('suffix'):
      suffix_data=request.args.get('suffix')
      for k in kv_store:
        if k.endswith(suffix_data):
          sorted_data[k]=kv_store[k]
    else:
      return "No prefix or suffix data"
    return jsonify(sorted_data)
  except:
    return "Search function Error"

@app.route("/get/<key>")
def get_value(key):
  try:
    if key in kv_store:
      return kv_store[key]
    else:
      return "Key Not present"
  except:
    return "get function Error"

@app.route("/set",methods=['POST'])
def set():
  try:
    request_data = request.json
    for i in request_data:
      view_metric.inc()               # Increament counter for total_no_of_keys_total 
      kv_store[i]=request_data[i]
    return "JSON posted"
  except:
    return "JSON not posted"

@app.route("/health")
def stats_health():
  return "OK"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='8000')

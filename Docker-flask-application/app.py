from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "<center><h1>Flask Sample Application - Version1</h1></center>"


app.run(debug=True,host='0.0.0.0',port='5000')

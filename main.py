from flask import Flask, render_template, request
import datafile


app = Flask(__name__, static_folder='/static')
app.config['SECRET_KEY'] = datafile.storedkey

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,host= '0.0.0.0',port=8888)

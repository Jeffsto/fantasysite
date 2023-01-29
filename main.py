from flask import Flask, render_template, request


app = Flask(__name__, static_folder='/static')

@app.route("/")
def index():
    return "<p>Main Page<p>"

if __name__ == "__main__":
    app.run(debug=True,host= '0.0.0.0',port=8888)

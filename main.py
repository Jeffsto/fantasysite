from flask import Flask, render_template, request


app = Flask(__name__, static_folder='/static')
app.config['SECRET_KEY'] = 'd460d5d24f58676ada118f6a'

@app.route("/")
def index():
    return "<p>Main Page<p>"

if __name__ == "__main__":
    app.run(debug=True,host= '0.0.0.0',port=8888)

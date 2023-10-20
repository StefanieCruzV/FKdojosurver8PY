
from crypt import methods
import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'page'




@app.route('/')
def index():
   
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

import os
from flask import Flask, render_template

# static_folder='static' ekleyerek Flask'a yerini kesin olarak söylüyoruz
app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

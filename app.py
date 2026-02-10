import os
from flask import Flask, render_template

# Dosya yollarını işletim sistemine göre otomatik ayarlar
app = Flask(__name__, 
            static_url_path='/static', 
            static_folder='static')

@app.route('/')
def home():
    # Templates klasöründeki index.html'i çağırır
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

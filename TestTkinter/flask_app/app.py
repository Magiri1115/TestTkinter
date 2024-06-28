from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_time')
def get_time():
    now = datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H:%M:%S")
    return current_time

if __name__ == '__main__':
    app.run(debug=True)

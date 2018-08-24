
from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ztou')
def ztou():
    return render_template('ztou.html')

@app.route('/ztow')
def ztow():
    return render_template('ztow.html')

@app.route('/wtou')
def wtou():
    return render_template('wtou.html')

@app.route('/wtoz')
def wtoz():
    return render_template('wtoz.html')

@app.route('/utow')
def utow():
    return render_template('utow.html')

@app.route('/utoz')
def utoz():
    return render_template('utoz.html')

if __name__ == '__main__':
    app.run(debug=True)

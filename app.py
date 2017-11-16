from flask import Flask, render_template, request
from data import call_meteorite

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods = ['GET'])
def search():
    search = request.args.get('search', None)
    m_class, mass, fall, year, geolocation = call_meteorite.call(search)
    return render_template('search.html', search=search, m_class=m_class, mass=mass, fall=fall, year=year, location=geolocation)

if __name__ == "__main__":
    app.run(debug=True)

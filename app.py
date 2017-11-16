from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods = ['GET'])
def search():
    search = request.args.get('search', None)
    return render_template('search.html', search=search)

if __name__ == "__main__":
    app.run(debug=True)

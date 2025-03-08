from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    lat = .1234
    lon = .5678
    return render_template('index.html', latitude=lat, longitude=lon)

if __name__ == '__main__':
    app.run(debug=True)

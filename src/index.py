from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/quien')
def quien():
    return render_template('quien.html')


@app.route('/trabajo')
def trabajo():
    return render_template('trabajo.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/Bibliografia')
def Bibliografia():
    return render_template('about.html')


@app.route('/Trabajo')
def Trabajo():
    return render_template('trabajo.html')


@app.route('/Contacto')
def Contacto():
    return render_template('contacto.html')


#if __name__ == '__main__':
#    app.run(debug=True)

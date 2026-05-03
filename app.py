from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def contact():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/france")
def france():
    return render_template('france.html')

@app.route("/japan")
def japan():
    return render_template('japan.html')

@app.route("/italy")
def italy():
    return render_template('italy.html')

@app.route("/spain")
def spain():
    return render_template('spain.html')

@app.route("/greece")
def greece():
    return render_template('greece.html')

@app.route("/german")
def german():
    return render_template('german.html')

@app.route("/arabic")
def arabic():
    return render_template('arabic.html')

@app.route("/georgia")
def georgia():
    return render_template('georgia.html')

@app.route("/usa")
def usa():
    return render_template('usa.html')

@app.route("/uk")
def uk():
    return render_template('uk.html')

@app.route("/ireland")
def ireland():
    return render_template('ireland.html')

@app.route("/turkey")
def turkey():
    return render_template('turkey.html')

@app.route("/canada")
def canada():
    return render_template('canada.html')

if __name__ == "__main__":
    app.run(debug=True)
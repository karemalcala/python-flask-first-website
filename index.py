from flask import Flask, render_template

app = Flask(__name__)

# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/products', strict_slashes=False)
def products():
    return render_template("products.html")

""" @app.route('/*')
def products():
    return render_template("error.html") """

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)

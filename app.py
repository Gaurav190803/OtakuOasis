from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shop')
def shop():
     return render_template('shop.html')

@app.route('/sproduct')
def sproduct():
     return render_template('sproduct.html')



if __name__ == "__main__":
    app.run(debug=True,port=8000)
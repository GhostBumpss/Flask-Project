from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/about/<name>')
def aboute_page(name):
    return f'<h1>About Page {name}</h1>'

@app.route('/market')
def market_page():
    items_list = [
        {'id': 1, 'name': 'Phone', 'barcode': '9674021332', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '9038122689', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '1234567890', 'price': 50}
    ]
    return render_template('market.html', items=items_list)
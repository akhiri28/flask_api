from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {'item': 'shoes', 'price': 2000},
            {'item': 'crocks', 'price': 1000}
        ]
    }


]

@app.route('/store')
def get_stored():
    return {'stores': stores}

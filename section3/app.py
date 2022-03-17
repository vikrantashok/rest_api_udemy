from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [{
    'name': 'My Store',
    'items': [{'name':'my item', 'price': 15.99 }]
}]


@app.route('/')
def home():
  return render_template('index.html')



#POST
@app.route("/store", methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = { 
        'name' : request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'massage': 'store not found'})

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})


#POST
@app.route("/store/<string:name>/item", methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'massage': 'store not found'})


#GET
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'item': store['items']})
    return jsonify({'massage': 'store not found'})    

app.run(port=5000)
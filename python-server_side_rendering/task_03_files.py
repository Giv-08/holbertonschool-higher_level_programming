from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)

        item_list = data.get("items", [])
    # "items" can be accessed in items.html
    return render_template('items.html', items=item_list)

@app.route('/contact')
def contact():
    return render_template('contact.html')

# read json
def read_json():
    with open('.templates/products.json', 'r') as file:
        data = json.load(file)
    return data
# read csv
def read_csv():
    with open('products.csv', 'r') as file:
        product_list = []
        csv_file = csv.DictReader(file)
        for row in csv_file:
            row['id'] = int(row['id'])
            row['price'] = int(row['price'])
            product_list.append(row)
    return product_list

# route /products
@app.route('/products')
def products():

    source = request.args.get('source')
    p_id = request.args.get('p_id')

    if source == 'json':
        products = read_json
    elif source == 'csv':
        products = read_csv
    else:
        return render_template('contact.html', "Wrong source")

    if p_id:
        try:
            p_id = int(p_id)
            products = [product for product in products if product['id'] == p_id]
            if not products:
                return render_template('product_display.html', "Product not found")
        except ValueError:
            return render_template('product_display.html', "Id invalid")

if __name__ == '__main__':
    app.run(debug=True, port=5000)

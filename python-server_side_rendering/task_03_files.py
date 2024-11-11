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

# read json
def read_json():
    with open('products.json', 'r') as file:
        data = json.load(file)
    return data
# read csv
def read_csv():
    with open('products.csv', newline='', encoding='utf-8') as file:
        product_list = []
        csv_file = csv.DictReader(file)
        for row in csv_file:
            # row['id'] = int(row['id'])
            # row['price'] = int(row['price'])
            product_list.append(row)
    return product_list

# route /products
@app.route('/products', methods=['GET'])
def products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')

    # Validate the source parameter
    if source not in ['json', 'csv']:
        error_message = "Wrong source"
        return render_template('product_display.html', error=error_message)

    # Read data based on source
    if source == 'json':
        products = read_json()
    else:
        products = read_csv()

    # Filter by product id if provided
    if product_id:
        product_found = False
        filtered_products = []
        for product in products:
            if str(product.get('id')) == product_id:
                filtered_products.append(product)
                product_found = True
        if not product_found:
            error_message = "Product not found"
            return render_template('product_display.html', error=error_message)
        products = filtered_products

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

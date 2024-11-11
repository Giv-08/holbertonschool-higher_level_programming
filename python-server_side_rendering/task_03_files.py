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
# def read_json():
#     with open('products.json', 'r') as file:
#         data = json.load(file)
#     return data
# # read csv
# def read_csv():
#     with open('products.csv', newline='', encoding='utf-8') as file:
#         product_list = []
#         csv_file = csv.DictReader(file)
#         for row in csv_file:
#             # row['id'] = int(row['id'])
#             # row['price'] = int(row['price'])
#             product_list.append(row)
#     return product_list
def read_json():
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []

# Function to read CSV data
def read_csv():
    try:
        products = []
        with open('products.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append(row)
        return products
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

# route /products
@app.route('/products', methods=['GET'])
def products():

    source = request.args.get('source').lower()
    p_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', "Wrong source")

    if source == 'json':
        products = read_json
    elif source == 'csv':
        products = read_csv

    if p_id:
        product_found = False
        filtered_products = []
        for product in products:
            if str(product.get('id')) == p_id:
                filtered_products.append(product)
                product_found = True
        if not product_found:
            error_message = "Product not found"
            return render_template('product_display.html', error=error_message)
        products = filtered_products

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

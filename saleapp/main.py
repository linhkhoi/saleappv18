from flask import render_template
from saleapp import app, utils


@app.route('/')
def index():
    categories = utils.read_data()
    return render_template('index.html',
                           categories=categories)

#  https://github.com/duonghuuthanh/saleappv44.git

@app.route('/products')
def list_product():
    product = utils.read_data("data/products.json")
    return render_template('list-products.html',
                           product=product)


if __name__ == '__main__':
    app.run(debug=True)
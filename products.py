from bottle import route, run

@route('/products')
def products(self):
    return "This should show the product listing"

@route('/products/:id')
def product(self):
    return "This should show a product with id"

run(host='localhost', port=8080, debug=True)
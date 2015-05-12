from bottle import route, run, get, post, request

@get('/products')
def products():
    return "This should show the product listing"

@get('/products/<id>')
def product(id=-1):
    return "This should show a product with id ", id

run(host='localhost', port=8080, debug=True, reloader=True)
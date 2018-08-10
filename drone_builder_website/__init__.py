from flask import Flask
app = Flask(__name__)


#blueprin
from drone_builder_website.views import products
from drone_builder_website.views import build_form

app.register_blueprint(products.mod)
app.register_blueprint(build_form.mod)

@app.route('/')
def hello_world():
    return 'Hello, World!'

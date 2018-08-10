from flask import Flask
from drone_builder_website.views import products

app = Flask(__name__)


#blueprin
app.register_blueprint(products.mod)


@app.route('/')
def hello_world():
    return 'Hello, World!'

from flask import Blueprint, render_template, jsonify

mod = Blueprint('products', __name__, url_prefix='/products')

@mod.route('/')
def index():
    return render_template('products/index.html')


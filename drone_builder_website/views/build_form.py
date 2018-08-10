from flask import Blueprint, render_template, jsonify

mod = Blueprint('build_form', __name__, url_prefix='/build_form')

@mod.route('/')
def index():
    return render_template('build_form/index.html')


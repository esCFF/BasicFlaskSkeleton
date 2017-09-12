from flask import render_template, Blueprint, request

index = Blueprint('index', __name__, template_folder='templates', static_folder='static')

@index.route('/')
def home():
    return render_template('/home.html', data={'title': 'Basic Flask Skeleton'})


@index.route('thinks')
def thinks():
    return render_template('/thinks.html', data={'title': 'Basic Flask Skeleton'})

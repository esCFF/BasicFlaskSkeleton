from flask import Flask
from app.config import DevelopmentConfig
from app.app import index


class CustomFlask(Flask):
    """ Jinja2 and vueJs cohabitation """
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='(%',
        block_end_string='%)',
        variable_start_string='((',
        variable_end_string='))',
        comment_start_string='(#',
        comment_end_string='#)',
        ))


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# API endpoints

#####

# APP routes
app.register_blueprint(index, url_prefix="/")
#########
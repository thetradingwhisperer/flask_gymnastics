from my_app.hello.models import MESSAGES
from flask import render_template, request, Blueprint

hello = Blueprint('hello', __name__)

@hello.route('/')
@hello.route('/hello')
def hello_world():
    user = request.args.get('user', 'Arsene') # second args is a default value
    return render_template('index.html', user=user)

@hello.route('/show/<key>')
def get_message(key):
    return MESSAGES.get(key) or "%s not found!" % key

@hello.route('/add/<key>/<message>')
def add_or_update_message(key, message):
    MESSAGES[key] = message
    return "%s Added/Updated" % key
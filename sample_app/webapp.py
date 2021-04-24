import pathlib

import jinja2
from flask import Flask, Markup, render_template

from flask_wtf import FlaskForm
from flask_codemirror.fields import CodeMirrorField
from wtforms.fields import SubmitField

import flask_codemirror

DIRECTORY_OF_THIS_FILE = pathlib.Path(__file__).parent

# https://www.ckwnc.com/ UML editor
# https://cdnjs.com/libraries/codemirror


from flask import Flask
from flask_codemirror import CodeMirror
# # mandatory
# CODEMIRROR_LANGUAGES = ['yaml']
# WTF_CSRF_ENABLED = True
# SECRET_KEY = 'secret'
# # optional
# CODEMIRROR_THEME = '3024-day'
# CODEMIRROR_ADDONS = (
#         # ('ADDON_DIR','ADDON_NAME'),
# )
# CODEMIRROR_VERSION = '5.61.0'
app = Flask(__name__)
# app.config.from_object(__name__)

# app = Flask(__name__)  # pylint: disable=invalid-name
# This will force exceptions when a variable is missing in a template
app.jinja_env.undefined = jinja2.StrictUndefined
app.secret_key = b'_6#y2L"F4Q8z\n\xec]/'
app.config["CODEMIRROR_LANGUAGES"] = ['yaml', 'python']
app.config["WTF_CSRF_ENABLED"] = True
app.config["CODEMIRROR_THEME"] = ''
# '', default: perfect - clear, calm
# 'neat', ok - calm
# 'idea', perfect - clear and calm
# 'erlang-dark', perfect - very colorful
# 'eclipse' perfect
# 'dracula' ok, howerever background is gray
# 'colorforth' average
# 'cobalt' average
# '3024-day' average

app.config["CODEMIRROR_ADDONS"] = (
    ('merge', 'merge'),
    # ('fold', 'foldcode'),
    # ('fold', 'foldgutter'),
    # ('fold', 'indent-fold'),
)
app.config["CODEMIRROR_VERSION"] = '5.61.0'

codemirror = CodeMirror(app)

CODEMIRROR_CONFIG = {
    'lineNumbers': 'true',
}

class MyForm(FlaskForm):
    source_code = CodeMirrorField(language='yaml', config=CODEMIRROR_CONFIG)
    submit = SubmitField('Submit')

SAMPLE_TEXT = '''---

array:
  - 132
  - 2.434
  - 'abc'

list_of_lists:
  - [1, 2, 3]
  - [4, 5, 6]

my_hash:
  subkey:
    subkey1: 5
    subkey2: 6
  another:
    somethingelse: 'Important!'
'''

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        text = form.source_code.data
    else:
        form.source_code.data = SAMPLE_TEXT
    return render_template('index.html', form=form)

@app.route('/merge')
def merge():
    return render_template('merge.html')

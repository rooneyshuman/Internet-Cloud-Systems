"""
A Flask application for viewing and submitting bubble tea store locations
"""
import flask
from flask.views import MethodView
from index import Index
from form import Form
from shops import Shops

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/form/',
                 view_func=Form.as_view('form'),
                 methods=['GET', 'POST'])

app.add_url_rule('/shops/',
                 view_func=Shops.as_view('shops'),
                 methods=["GET"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

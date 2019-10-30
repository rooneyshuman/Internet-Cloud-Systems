from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Form(MethodView):
    def get(self):
        return render_template('form.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['name'], request.form['street'], request.form['city'], request.form['state'],
                     request.form['zip'], request.form['open_hr'], request.form['close_hr'], request.form['phone'],
                     request.form['drink'], request.form['rating'])
        return redirect(url_for('shops'))

from __future__ import print_function # In python 2.7

from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
import sys

class Shops(MethodView):
    def get(self):
        model = gbmodel.get_model()
        shops = [dict(name=row[0], street=row[1], city=row[2], state=row[3], zip=row[4], open_hr=row[5],
                        close_hr=row[6], phone=row[7], drink=row[8], rating=row[9], website=row[10]) for row in model.select()]
        return render_template('shops.html', shops=shops)

    def post(self):
        model = gbmodel.get_model()
        model.delete(request.form['name'])

        return redirect(url_for('shops'))